from math import floor
import random
import time
from typing import Type
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib3 import Retry
from requests.adapters import HTTPAdapter
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pandas import DataFrame


class ScrapingUsedCarDataService:
    def __init__(self) -> None:
        pass

    timeout_count = 0

    def init_BeautifulSoup(self, url: str):
        random_seconds = random.uniform(0.001, 0.01)
        time.sleep(random_seconds)

        session = requests.Session()

        retries = Retry(total=5,
                        backoff_factor=1,
                        status_forcelist=[500, 502, 503, 504])

        session.mount("https://", HTTPAdapter(max_retries=retries))

        try:
            # timeout対策 -> https://blog.cosnomi.com/posts/1259/
            # session追加 -> https://qiita.com/azumagoro/items/3402facf0bcfecea0f06
            res = session.get(url, timeout=30)
        except (requests.exceptions.Timeout, requests.Timeout):
            print(f'error res: {res}')
            if self.timeout_count < 4:
                self.init_BeautifulSoup(url)
                self.timeout_count += 1

        res.encoding = res.apparent_encoding
        return BeautifulSoup(res.content, 'lxml')

    def get_all_used_car_overview_url_list(self, url: str):
        bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
            self, url=url
        )

        # h3の[0]を取得して合計台数を取得
        # 合計/50の切り捨てでページ数算出 -> url_index = i + 2 で換算

        # url -> 'https://www.goo-net.com/usedcar/bodytype-KEI/'
        count_html = bs_res.find_all('span', {'class': 'count'})[0]
        all_count = int(
            count_html.get_text().replace(',', '')
        )
        overview_url_list = [url]

        ### 本番用 ###
        overview_url_length = floor(all_count / 50)

        ### テスト用 ###
        # overview_url_length = 3

        ### さらに分割してページを取得するためにrangeを指定する ###
        # start_range, end_range = 0, 500  # -> doing lab_desktop and doing left_3
        start_range, end_range = 501, 1000  # -> doing left_1
        # start_range, end_range = 1001, 1500  # -> doing left_2
        # start_range, end_range = 1501, 2000  # -> done
        # start_range, end_range = 2001, 2500  # -> done
        # start_range, end_range = 2501, 3000 -> done
        # start_range, end_range = 3001, 3500 -> done
        # start_range, end_range = 0, overview_url_length

        for i in range(overview_url_length):
            if start_range <= i and i <= end_range:
                url_index = i + 2

                ### 全軽自動車取得用 ###
                current_url = f'https://www.goo-net.com/usedcar/bodytype-KEI/index-{url_index}.html'

                ### brand-MITSUBISHI/car-EK_WAGON only ###
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_WAGON/index-{url_index}.html'
                # ek-カスタム
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_CUSTOM/index-{url_index}.html'
                # ek-クロス
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_X/index-{url_index}.html'
                # ek-スペース
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPACE/index-{url_index}.html'
                # ek-スペースカスタム
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPACE_CUSTOM/index-{url_index}.html'
                # ek-クロススペース
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_X_SPACE/index-{url_index}.html'
                # ek-スポーツ
                # current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPORT/index-{url_index}.html'

                overview_url_list.append(current_url)

        detail_page_url_list = []
        for overview_url in (tqdm(overview_url_list)):
            cu_bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
                self, url=overview_url
            )

            data_wrapper_list_html = cu_bs_res.find_all(
                'div', {'class': 'data-wrapper'}
            )

            for j in range(50):
                if j < len(data_wrapper_list_html)-1:
                    data_wrapper_html = data_wrapper_list_html[j]
                    h3_html = data_wrapper_html.find('h3')
                    detail_page_href = h3_html.find('a').get('href')
                    is_gookantei = data_wrapper_html.find(
                        'dd', {'class': 'gookantei02'}
                    )
                    # Goo鑑定があれば詳細ページURLを取得する
                    if is_gookantei != None:
                        detail_page_url = 'https://www.goo-net.com' + detail_page_href
                        detail_page_url_list.append(detail_page_url)

        return detail_page_url_list

    def get_detail_page_data(self, detail_url: str):
        bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
            self, url=detail_url
        )

        # 価格を取得
        price_text_list = self.get_price_text_list(bs_res, detail_url)
        price_text_list.insert(0, detail_url)

        ### 車両詳細を取得 ###
        ### status_block_list: [0~2]は車両の基本情報, [3]以降が全てon offのやつ ###
        status_block_list = self.get_status_block_text(bs_res)

        # アフターサービスを取得
        # data: {'補償': 1, '法定整備': 1}
        after_service_list = self.get_after_service_list(bs_res, detail_url)

        # goo鑑定を取得
        # data: {'外装': '4', '内装': '4', '機関': '正常', '修復歴': '無し'}
        goo_kantei_hyouka_list = self.get_goo_kantei_hyouka_list(bs_res)

        # return {'price_text_dict': price_text_dict, 'status_block_list': status_block_list, 'after_service_dict': after_service_dict, 'goo_kantei_hyouka_dict': goo_kantei_hyouka_dict}
        return price_text_list + status_block_list + after_service_list + goo_kantei_hyouka_list

    def get_price_text_list(self, bs_res: BeautifulSoup, url: str):
        # 万円が入っていたら順番に取得(0->本体価格,1->支払総額)
        price_html_list = bs_res.find('table', {'class': 'mainData'})
        if price_html_list == None:
            print('detail url: ', url)
            return []

        price_text_list = price_html_list.get_text().split()

        res_list = []
        for price_text in price_text_list:
            if '万円' in price_text:
                res_list.append(price_text)

        return res_list

    def get_status_block_text(self, bs_res: BeautifulSoup):
        status_block_list_html = list(bs_res.find_all(
            'div', {'class': 'statusBlock'})
        )
        status_block_title = []
        status_block_list = []
        status_block_val_dict = {
            '走行距離': '', '走行距離': '', '登録済未使用車': '', '禁煙車': '', '車検': '', '年式（初度登録）': '', '排気量': '', '乗車定員': '', '駆動方式': '', '燃料': '', 'ドア': '', 'ミッション': '', '過給器': '', '車体色': '', '車台番号下3桁': '', 'その他仕様': '', '全体のサイズ': '', '荷台寸法': '', '全長×全幅×全高': '', '車両重量': '', '駆動形式': '', '使用燃料': '', '最高出力': '', 'WLTCモード燃費': '', 'JC08モード燃費': '', '10/15モード燃費': ''
        }
        for i, status_block_html in enumerate(status_block_list_html):
            status_block = list(status_block_html.get_text().split())
            if i < 3:
                # status_list_html[0~2]は車両の基本情報
                status_block_title.append(status_block[0])
                new_status_block = [
                    item for item in status_block[1:] if '装備略号／用語解説' not in item and '※新車時のカタログデータとなります。実際とは異なる場合がございますので、詳細は販売店にご確認ください。'not in item and 'カタログで車種情報を詳しく見る' not in item and '内燃機関へ空気を強制的に送り込む装置。ターボ、スーパーチャージャーなどが該当' not in item
                ]

                for j, status in enumerate(new_status_block):
                    for status_title in status_block_val_dict:
                        if status in status_title:
                            status_block_val_dict[status_title] = new_status_block[j+1]

            # else:
            #     # status_list_html[3]以降が全てon offのやつ
            #     # -> :があった場合は区切るようにする。:以降は消す
            #     # -> これはそれぞれのstatusBlockで(on off4パターン)を頑張って切り分ける

            #     split_word = '：'
            #     status_block_title.append(status_block[0])
            #     li_list_res = status_block_html.find_all('li')
            #     li_html_list = []
            #     for li in li_list_res:
            #         li_html_list.append(li)

            #     # HTML状態のliのvalueを対処する

            #     status_block_list.append(li_html_list)

        status_block_list = [
            item for item in list(status_block_val_dict.values())
        ]

        return status_block_list

    def my_index(self, l, x, default=False):
        if x in l:
            return l.index(x)
        else:
            return default

    def get_after_service_list(self, bs_res: BeautifulSoup, url: str):
        # 補償の有無で判断(ダミー)、整備込みかどうか
        after_service_html = bs_res.find(
            'div', {'class': 'afterServiceBlock'}
        )
        if after_service_html == None:
            print('(get_after_service_list) detail url: ', url)
            return []
        after_service_list = after_service_html.find(
            'table').get_text().split()

        dummy_guarantee = 0
        if '保証付' in after_service_list[1]:
            dummy_guarantee = 1

        dummy_maintenance = 1
        if self.my_index(l=after_service_list, x='整備込') == False:
            dummy_maintenance = 0

        return [dummy_guarantee, dummy_maintenance]

    # class: qualityInnetTitle, qualityRank1, qualityRank2を取得
    # 1,2はtableの段の違いで、
    # 外装: qualityRank1[0], 内装: qualityRank1[1], 機関: qualityRank2[0], 修復歴: qualityRank2[1]
    def get_goo_kantei_hyouka_list(self, bs_res: BeautifulSoup):
        goo_kantei_hyouka_html = bs_res.find(
            'div', {'class': 'gooKanteiHyoukaTable'}
        )

        if goo_kantei_hyouka_html == None:
            return []

        quality_rank_1_list = goo_kantei_hyouka_html.find_all(
            'span', {'class': 'qualityRank1'}
        )
        quality_rank_2_list = goo_kantei_hyouka_html.find_all(
            'span', {'class': 'qualityRank2'}
        )
        res_list = []
        if quality_rank_1_list == [] or quality_rank_2_list == []:
            return []
        else:
            quality_rank_1_list = [
                item.get_text() for item in quality_rank_1_list
            ]
            quality_rank_2_list = [
                item.get_text() for item in quality_rank_2_list
            ]

            res_list = [
                quality_rank_1_list[0],
                quality_rank_1_list[1],
                quality_rank_2_list[0],
                quality_rank_2_list[1],
            ]

        return res_list

        res_list = []

    def _get_mm_html(self, row):
        url = row[2].value
        bs_res = self.init_BeautifulSoup(url)

        maker_html = bs_res.find('span', {'class': 'mainTit'})
        model_html = bs_res.find('p', {'class': 'tit'})
        if maker_html == None or model_html == None:
            return {'model': '', 'maker': ''}

        maker = maker_html.get_text().replace(' ', '')
        model = model_html.get_text().replace(' ', '')[
            len(maker)+1:]
        return {'model': model, 'maker': maker}

    def _get_mm_html_for_pd(self, data: str):
        url = data[2]
        bs_res = self.init_BeautifulSoup(url)

        maker_html = bs_res.find('span', {'class': 'mainTit'})
        model_html = bs_res.find('p', {'class': 'tit'})
        if maker_html == None or model_html == None:
            # print(f'url:{url}, empty')
            return ['', '']

        maker = maker_html.get_text().replace(' ', '')
        model = model_html.get_text().replace(' ', '')[len(maker)+1:].strip()
        # print(f'url:{url}, maker: {maker}, model: {model}')

        return [maker, model]

    def get_model_and_maker(self, list_data: list):
        with ProcessPoolExecutor() as executor:
            # INFO: 注意点として、純粋なfor文を使うとそんなに効果がないので必ずexecutor.mapを使って処理しよう！
            return list(tqdm(executor.map(self._get_mm_html_for_pd, list_data), total=len(list_data)))
