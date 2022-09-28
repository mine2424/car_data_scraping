
from turtle import color
from typing import Dict, List

from constants.openpyxl_constants import OpenPyxlConstants
from constants.constants import BASE_URL
from models.car_overview import CarOverview
from models.spec_table import SpecTable

#  test only
# from src.constants.openpyxl_constants import OpenPyxlConstants
# from src.constants.constants import BASE_URL
# from src.models.car_overview import CarOverview
# from src.models.spec_table import SpecTable

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from tqdm import tqdm
import random
import requests
from statistics import median, mean
import math


class ScrapingDataService:
    def __init__(self) -> None:
        pass

    random_seconds = random.uniform(0.234, 1.000)

    def init_BeautifulSoup(self, url: str):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        return BeautifulSoup(res.text, 'html.parser')

    def init_selenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        chrome_service = fs.Service(executable_path='../chromedriver')
        return webdriver.Chrome(service=chrome_service, options=options)

    def get_all_light_car_overview(self):
        """
            軽自動車の概要(url,name,maker)を全取得
        """

        # init_req = self.init_BeautifulSoup(
        init_req = ScrapingDataService.init_BeautifulSoup(
            # self, url='https://autos.goo.ne.jp/catalog/type/kei/',
            self, url='https://autos.goo.ne.jp/catalog/type/keirv/',
            #
            # self,   url='https://autos.goo.ne.jp/catalog/type/compact/'
            # 'https://autos.goo.ne.jp/catalog/type/minivan/'
            # 'https://autos.goo.ne.jp/catalog/type/sedan/'
            # 'https://autos.goo.ne.jp/catalog/type/coupe/',
        )
        all_car_url_by_light_car = init_req.find_all(
            'div', attrs={'class': 'item'},
        )

        car_overview_list = []

        for i, car in enumerate(all_car_url_by_light_car):
            # if i < 3:
            url = BASE_URL + car.find('a').get('href')
            title = car.find_all(
                'p', attrs={'class': 'title'})[0].get_text()
            manufacturer = car.find_all(
                'p', attrs={'class': 'manufacturer'})[0].get_text()

            car_overview_list.append(
                {'url': url, 'car_name': title, 'car_maker': manufacturer}
            )

        return car_overview_list

    def get_all_light_car_by_year(self, car_overview_list: List):
        """
            各軽自動車の指定の年式(2006~2021)を取得する
        """
        all_car_list_by_year = {}
        # 全車の全年式を取得
        for i, car_overview in enumerate(tqdm(car_overview_list)):
            # car_details_req = self.init_BeautifulSoup(
            car_details_req = ScrapingDataService.init_BeautifulSoup(
                self, url=car_overview['url']
            )
            all_years = car_details_req.find(
                'ul', attrs={'class': 'page-links js-page-scroll'}
            )
            year_urls = all_years.find_all('a')
            car_list_by_year = []

            car_name = car_overview['car_name']

            for i, year in enumerate(year_urls):
                year_text = str(year.get_text())
                year_num = int(year_text.replace('年', ''))
                if year_num >= 2006:  # and year_num <= 2021:
                    year_url = BASE_URL+year.get('href')
                    car_list_by_year.append(
                        {
                            'year_text': year_text,
                            'car_maker': car_overview['car_maker'],
                            'url': year_url
                        }
                    )

            all_car_list_by_year[car_overview['car_name']
                                 ] = car_list_by_year

        return all_car_list_by_year

    def get_car_grade(self, car_list_by_year: Dict):
        grade_list_by_all_year = []

        for i, car_years in enumerate(tqdm(car_list_by_year.values())):
            car_name = list(car_list_by_year.keys())[i]
            # 年ごとのリストを作成
            grade_dict_by_year = {}
            for j, car_year in enumerate(car_years):
                # 月ごとのリストが入っている
                most_high_grade_month_dict = ScrapingDataService.get_most_high_price_grade(
                    self, url=car_year['url'], car_maker=car_year['car_maker']
                )
                if car_name in grade_dict_by_year:
                    grade_dict_by_year[car_name].update(
                        most_high_grade_month_dict
                    )
                else:
                    grade_dict_by_year[car_name] = most_high_grade_month_dict

            grade_list_by_all_year.append(grade_dict_by_year)
        return grade_list_by_all_year

    def get_most_high_price_grade(self, url: str, car_maker: str):
        random_seconds = random.uniform(0.234, 1.000)
        time.sleep(random_seconds)

        car_grade_req = ScrapingDataService.init_BeautifulSoup(self, url=url)

        year_month_html_list = car_grade_req.find_all('h2')

        tables = car_grade_req.find_all('table')
        grade_list_by_table = []
        for table in tables:
            column_dict = {
                'grade_name_list': table.find_all('td', attrs={'class': 'num_02'}),
                'displacement_list': table.find_all('td', attrs={'class': 'num_03'}),
                'driven_list': table.find_all('td', attrs={'class': 'num_04'}),
                'fuel_consumption_list': table.find_all('td', attrs={'class': 'num_05'}),
                'price_list': table.find_all('td', attrs={'class': 'num_06'}),
            }
            grade_list_by_table.append(column_dict)

        year_month_list = []
        # print('year_month_html_list', year_month_html_list)
        for i, year_month in enumerate(year_month_html_list):
            year_month_text = year_month.get_text()

            year_idx = year_month_text.find('年')
            year = year_month_text[0:year_idx]
            month_idx = year_month_text.find('月')
            month = year_month_text[year_idx+1:month_idx]
            year_month_list.append(str(year+month).strip())

        all_grade_list_by_year = []
        max_price_idx_list_by_year = []
        for i, column_dict in enumerate(grade_list_by_table):
            all_grade_list_by_month = []
            price_list_by_month = []

            if len(year_month_list) == 0:
                print('url', url)
                print('tables', tables)
                print('0_year_month_list', year_month_list)
                print('column_dict', column_dict)

            for j, _ in enumerate(column_dict['grade_name_list']):
                price = int(
                    column_dict['price_list'][j].get_text()[:-1].replace(',', ''))
                grade_dict = {
                    'year_month': year_month_list[i],
                    'car_maker': car_maker,
                    'grade_name': column_dict['grade_name_list'][j].get_text(),
                    'displacement': column_dict['displacement_list'][j].get_text(),
                    'driven': column_dict['driven_list'][j].get_text(),
                    'fuel_consumption': column_dict['fuel_consumption_list'][j].get_text(),
                    'price': price,
                    'url': BASE_URL + column_dict['grade_name_list'][j].find('a').get('href')
                }
                all_grade_list_by_month.append(grade_dict)
                price_list_by_month.append(price)

            all_grade_list_by_year.append(all_grade_list_by_month)

            # ここで値段の最大値を取得している
            # choiced_val = self.choice_max_price_in_grades(
            #     price_list_by_month=price_list_by_month
            # )

            # ここで最小値を取得
            # choiced_val = self.choice_min_price_in_grades(
            #     price_list_by_month=price_list_by_month
            # )

            # ここで中央値-平均で一番近い値を取得している
            # choiced_val = self.choice_near_median_price_in_grades(
            #     price_list_by_month=price_list_by_month
            # )

            # max_price_idx_list_by_year.append(
            #     price_list_by_month.index(choiced_val)
            # )

        max_price_column_dicts = {}
        for i, _grade_list_by_month in enumerate(all_grade_list_by_year):
            # 特定のグレードを取得する場合(最小、最大)
            # max_price_idx = max_price_idx_list_by_year[i]
            # max_price_column_dict = _grade_list_by_month[max_price_idx]
            # max_price_column_dicts[max_price_column_dict['year_month']
            #                        ] = max_price_column_dict

            # 全グレードを取得
            max_price_column_dicts[_grade_list_by_month[0]['year_month']
                                   ] = _grade_list_by_month

        return max_price_column_dicts

    def choice_min_price_in_grades(self, price_list_by_month: list):
        return min(price_list_by_month)

    def choice_max_price_in_grades(self, price_list_by_month: list):
        return max(price_list_by_month)

    def choice_near_median_price_in_grades(self, price_list_by_month: list):
        price_list_by_month_len = len(price_list_by_month)
        price_list_by_month_smaller_med = math.floor(
            price_list_by_month_len / 2
        )-1
        price_list_by_month_higher_med = price_list_by_month_smaller_med+1
        mea = mean(price_list_by_month)
        med = median(price_list_by_month)
        smaller_val = price_list_by_month[price_list_by_month_smaller_med]-mea
        higher_val = price_list_by_month[price_list_by_month_higher_med]-mea
        if higher_val < smaller_val:
            med = price_list_by_month[price_list_by_month_higher_med]
        else:
            med = price_list_by_month[price_list_by_month_smaller_med]

        return med

    def get_light_car_details(self, grade_list_by_all_year):
        all_details_list = []
        for i, grade_list_by_year in enumerate(tqdm(grade_list_by_all_year)):
            for j, grade_car_overview in enumerate(grade_list_by_year.values()):
                for y, column_dict_list in enumerate(grade_car_overview.values()):
                    # 特定のグレードのみの場合
                    # all_value_for_excel = self.set_car_detail_value(
                    #     grade_list_by_year=grade_list_by_year, column_dict=column_dict_list
                    # )
                    # all_details_list.append(all_value_for_excel)

                    # 全取得する場合
                    for z, column_dict in enumerate(column_dict_list):
                        all_value_for_excel = self.set_car_detail_value(
                            grade_list_by_year=grade_list_by_year, column_dict=column_dict
                        )
                        all_details_list.append(all_value_for_excel)

        return all_details_list

    def set_car_detail_value(self, grade_list_by_year: list, column_dict: dict):
        # if column_dict['car_maker'] != 'ＢＭＷ':
        # car_details_req = self.init_BeautifulSoup(
        car_details_req = ScrapingDataService.init_BeautifulSoup(
            self,   url=column_dict['url']
        )

        all_tables = car_details_req.find_all(
            'table', attrs={'class': 'tables bordered'}
        )
        car_details_title = []
        car_details_value = []
        isFetchTitle = False
        normal_color_count = 0
        option_color_count = 0

        # constantsにあるtitleを元に削っていく
        # car_details_titleとnature_necessary_titlesで一致した値があったらcar_details_titleのidxを返す
        # そのidxを元にcar_details_titleとcar_details_valueの値を返す
        for y, table in enumerate(all_tables):
            if y == len(all_tables)-1:
                table_td = table.find_all('td')
                for t, val in enumerate(table_td):
                    t = t + 1
                    val = val.get_text()
                    if t % 2 == 0:
                        if val.isspace() == False:
                            option_color_count = option_color_count+1
                    else:
                        if val.isspace() == False:
                            normal_color_count = normal_color_count+1
            if len(all_tables) != y:
                striped_table = table.get_text().split()
                for val in striped_table:
                    if isFetchTitle:
                        car_details_value.append(val)
                    else:
                        car_details_title.append(val)
                    isFetchTitle = not isFetchTitle

        kNature_necessary_titles = OpenPyxlConstants.nature_necessary_titles
        title_idx_list = []

        # 色以外のtitle indexを取得
        for i, title in enumerate(car_details_title):
            for j, nature_necessary_title in enumerate(kNature_necessary_titles):
                if title == nature_necessary_title:
                    title_idx_list.append(i)

        new_car_details_value = []
        for idx in title_idx_list:
            new_car_details_value.append(
                car_details_value[idx])

        # いいやつ
        # car_details_value['6,880,000円', '15万円～828万円', 'ステーションワゴン', '2760mm', '5ドア', '1500/1515mm', '5名', '－', 'ABA-VS35', '1690kg', '4525×1815×1450mm', 'N54B30A', '直列6気筒DOHCツインターボ', '－', '2979cc', '10.2', 'デジタル・モーター・エレクトロニクス(DME/電子燃料噴射装置)', '225kW(306ps)/5800rpm', '400N・m(40.8kg･m)/1300～5000rpm', 'ツインターボ', '60リットル', '無鉛プレミアムガソリン', '8.6km/リットル', 'パワーアシスト付きラック＆ピニオン', '5.3m', 'ダブル・ジョイント・スプリング・ストラット式、コイル・スプリング、スタビライザー', '5リンク式、コイル・スプリング、スタビライザー', 'ベンチレーテッドディスク', 'ベンチレーテッドディスク', '225/45R17', '225/45R17', '5名', '電子油圧制御式6速AT', 'FR', '－', '－', '4.171', '2.340', '1.521', '1.143', '0.867', '0.691','－', '－', '3.403', '－', '－', '標準', '標準', '標準', '－', '－', '－', '－', '標準', '標準', '標準', '標準', '標準', '標準', '標準', '標準', '－', '標準', '－', '－', '－', '標準', 'CBC／コーナリング・ブレーキ･コントロール', 'ナビゲーション', 'ナビゲーションメディア', 'サウンド（カセット&MD）', 'CDプレイヤー', 'エアコン', 'パワーウィンドウ', '集中ドアロック', 'ステアリングホイールテレスコピック機構', 'ステアリングホイールチルト機構', 'クルーズコントロール', '本革巻きステアリング', '本革シート', '前席パワーシート', '後席パワーシート', 'ウッドパネル', 'サン／ムーンルーフ', 'アルミホイール', '分割可倒式リアシート', 'UVカットガラス', 'プライバシーガラス', '色系統', 'メーカーオプション', 'ブラックII（ソリッド・カラー）', '白系', '緑系', 'マルーン（茶）系', 'オリーブ系', 'モナコ・ブルー（メタリック・カラー）', '灰系', '黄系', 'シアン系', '銀系', '赤系', '青系', 'テール系', '金系']
        # new_car_details_value['6,880,000円', 'ステーションワゴン', '5名', 'ABA-VS35', 'ABA-VS35', '1690kg', '4525×1815×1450mm', 'N54B30A','直列6気筒DOHCツインターボ', '－', '2979cc', '225kW(306ps)/5800rpm', 'ツインターボ', '8.6km/リットル', '5名', '電子油圧制御式6速AT', '電子油圧制御式6速AT', 'FR']

        # だめなやつ
        # car_details_valueになぜかtitleになるものが入っている
        # car_details_value ['7,320,000円', '15万円～828万円', 'オープンカー', '2725mm', '2ドア', '1470/1480mm', '4名', '－', 'GH-AV30', '1680kg', '4490×1755×1370mm', '30', '種類', '内径×行程', '総排気量', '圧縮比', '燃料供給装置', '最高出力', '最大トルク', '過給機', '燃料タンク容量', '使用燃料', '燃費（10/15モードor10モードorJC08モード)', 'ステアリング形式', '最小回転半径', 'サスペンション前', 'サスペンション後', 'ブレーキ前', 'ブレーキ後', 'タイヤ前', 'タイヤ後', '乗員定員', '型式', '駆動方式', 'LSD', 'ＣＶＴ', '第1速', '第2速', '第3速', '第4速', '第5速', '第6速', '第7速', '第8速', '後退', '第1速', '第2速', 'フロントフォグランプ', 'リアフォグランプ', 'キセノンヘッドランプ', 'プロジェクターヘッドランプ', 'フロントスポイラー', 'リアスポイラー', 'リアワイパー', '運転席エアバック', '助手席エアバック', 'サイドエアバック', 'ＡＢＳ(アンチロックブレーキ)', 'トラクションコントロール', '前席シートベルトプリテンショナー', '前席シートベルトフォースリミッター', '後席３点式シートベルト', 'チャイルドシート固定機構付き後席シートベルト', 'サイドインパクトバー', 'ブレーキアシスト', '衝突安全ボディー', 'EBD（電子制動力配分装置）', '盗難防止システム', 'その他安全装備', 'DSC/ダイナミック･スタビリティ･コントロール', 'EBV/エレクトロニック･ブレーキ･フォース･ディストリビューション', '標準', 'DVD', 'AM/FMラジオ付きMDプレーヤー', '－', 'フルオート', '標準', '標準', '標準', '標準', '標準', '標準', '標準', '標準', '－', '標準', 'なし', '17インチ標準', '分割式', '－', '－', 'メーカー標準', '黒系', 'ブラック・サファイア（メタリック・カラー）', 'アルピン・ホワイトIII（ソリッド・カラー）', 'オックスフォード・グリーンII（メタリック・カラー）', 'ハバナ（メタリック・カラー）', '紺系', '紫系', 'シルバー・グレー（メタリック・カラー）orスパークリング・グラファイト（メタリック・カラー）', '黄緑系', 'マゼンダ系', 'スチール・ブルー（メタリック・カラー）orチタン・シルバー（メタリック・カラー）', 'ジャパン・レッド（ソリッド・カラー）', 'ミスティック・ブルー（メタリック・カラー）', 'パール系', 'ソノラ（メタリック・カラー）']
        # new_car_details_value ['7,320,000円', 'オープンカー', '4名', 'GH-AV30', 'GH-AV30', '1680kg', '4490×1755×1370mm', '30']

        # 原因
        # エンジン型式:	30 6S 30と6S間にスペースがはいていたためそれで切られていた

        # print('car_details_title', car_details_title)
        # print('car_details_value', car_details_value)
        # print('new_car_details_value', new_car_details_value)
        # print('column_dict', column_dict)
        # print(' ')
        # print(' ')

        car_name = list(grade_list_by_year.keys())[0]
        year = column_dict['year_month'][:4]
        month = column_dict['year_month'][4:]

        # all_length_list: ['全長','全幅','全高']
        all_length_list = str(new_car_details_value[6])[
            :-2].split('×')

        car_size = int(all_length_list[0]) * \
            int(all_length_list[1]) * \
            int(all_length_list[2]) / 10 ** 9

        # データ合併
        # '年','月' -> column_dict['year_month'], メーカー -> coulmn_dict['car_maker'], 台数 ->未入力でok, 通称名 -> list(grade_list_by_year.keys())[0], 型番 ->型式(new_car_details_value[2]),
        # 車種 -> 全部「乗用」にしとく, 新車価格 -> new_car_details_value[0], '実質価格(CPI2007基準)' -> 未入力でok, 排気量 -> column_dict['displacement']
        # トランスミッション -> column_dict['driven'], 乗車定員 -> new_car_details_value[1],ハイブリット -> 未入力でok, 最高出力(kW) -> new_car_details_value[10]
        # '燃費(WLTC)','燃費(JC08)','燃費(10.15)' -> 燃費（10/15モードor10モードorJC08モード)(new_car_details_value[11]),{'全長','全幅','全高'} -> new_car_details_value[4]でsplitする,
        # 'サイズ' -> '全長'×'全幅'×'全高'/10^9,'車両重量' -> new_car_details_value[3]

        # 修正版
        # new_car_details_value ['1,290,300円', '軽自動車', '4名', 'DBA-HA36S', 'DBA-HA36S', '700kg', '3395×1475×1500mm', 'R06A', '水冷直列3気筒DOHC12バルブ', '64.0mm×68.2mm', '658cc', 'EPI（電子制御燃料噴射装置）', '38kW(52ps)/6500rpm', 'なし', '－', '4名', '自動無段変速機', '自動無段変速機', 'FULL4WD', '標準']

        all_value_for_excel = {
            '年': year,
            '月': month,
            'メーカー': column_dict['car_maker'],
            '台数': '',
            '通称名': car_name,
            'グレード': column_dict['grade_name'],
            '型番': new_car_details_value[3],
            '車種': '乗用',
            '新車価格': (new_car_details_value[0][:-1]).replace(",", ""),
            '実質価格(CPI2007基準)': '',
            '排気量': column_dict['displacement'][:-2],
            'トランスミッション': column_dict['driven'],
            '乗車定員': new_car_details_value[2][:-1],
            'ハイブリット': '',
            '最高出力(kW)': new_car_details_value[11][:2],
            'メーカー標準ボディカラー': normal_color_count,
            'メーカーオプションボディカラー': option_color_count,
            '過給器': new_car_details_value[12],
            '燃費(WLTC)': new_car_details_value[13],
            '燃費(JC08)': new_car_details_value[13],
            '燃費(10.15)': new_car_details_value[13],
            '全長': all_length_list[0],
            '全幅': all_length_list[1],
            '全高': all_length_list[2],
            'サイズ': car_size,
            '車両重量': new_car_details_value[5][:-2],
        }

        return all_value_for_excel
