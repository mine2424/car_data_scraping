from math import floor
import random
import time
from typing import Type
import requests
from bs4 import BeautifulSoup


class ScrapingUsedCarDataService:
    def __init__(self) -> None:
        pass

    random_seconds = random.uniform(0.234, 1.000)

    def init_BeautifulSoup(self, url: str):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        return BeautifulSoup(res.text, 'html.parser')

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
        # overview_url_length = floor(all_count / 50)

        ### テスト用 ###
        overview_url_length = 1

        for i in range(overview_url_length):
            url_index = i + 2

            ### 全軽自動車取得用 ###
            # current_url = f'https://www.goo-net.com/usedcar/bodytype-KEI/index-{url_index}.html'

            ### brand-MITSUBISHI/car-EK_WAGON only ###
            current_url = f'https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_WAGON/index-{url_index}.html'

            overview_url_list.append(current_url)

        detail_page_url_list = []
        for overview_url in overview_url_list:
            random_seconds = random.uniform(0.234, 1.000)
            time.sleep(random_seconds)
            cu_bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
                self, url=overview_url
            )

            detail_page_url_list_html = cu_bs_res.find_all(
                'a', {'data-link-list': 'list_summary'}
            )

            for j in range(50):
                detail_page_a_tag = detail_page_url_list_html[j]
                detail_page_url = 'https://www.goo-net.com' + \
                    detail_page_a_tag.get('href')
                detail_page_url_list.append(detail_page_url)

        return detail_page_url_list

    def get_detail_page_data(self, detail_url: str):
        bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
            self, url=detail_url
        )

        # find_allにて仮に該当のものがなかったら[]で返される　

        # 価格を取得
        price_text_dict = self.get_price_text_dict(bs_res)

        ### 車両詳細を取得 ###
        ### status_block_list: [0~2]は車両の基本情報, [3]以降が全てon offのやつ ###
        status_block_list = self.get_status_block_text(bs_res)

        # アフターサービスを取得
        # data: {'補償': 1, '法定整備': 1}
        after_service_dict = self.get_after_service_dict(bs_res=bs_res)

        # goo鑑定を取得
        # data: {'外装': '4', '内装': '4', '機関': '正常', '修復歴': '無し'}
        goo_kantei_hyouka_dict = self.get_goo_kantei_hyouka_dict(bs_res=bs_res)

        return [price_text_dict, status_block_list, after_service_dict, goo_kantei_hyouka_dict]

    # 万円が入っていたら順番に取得(0->本体価格,1->支払総額)

    def get_price_text_dict(self, bs_res: BeautifulSoup):
        all_price_text_list = bs_res.find(
            'table', {'class': 'mainData'}
        ).get_text().split()
        res_dict = {'body_price': '', 'paied_price': ''}
        isBodyPrice = False
        for price_text in all_price_text_list:
            if '万円' in price_text:
                if isBodyPrice:
                    res_dict['paied_price'] = price_text
                else:
                    res_dict['body_price'] = price_text
                    isBodyPrice = not isBodyPrice

        return res_dict

    def get_status_block_text(self, bs_res: BeautifulSoup):
        status_block_list_html = list(bs_res.find_all(
            'div', {'class': 'statusBlock'})
        )
        status_block_title = []
        status_block_list = []
        for i, status_block_html in enumerate(status_block_list_html):
            status_block = list(status_block_html.get_text().split())
            if i < 3:
                # status_list_html[0~2]は車両の基本情報
                status_block_title.append(status_block[0])
                new_status_block = [
                    item for item in status_block[1:] if '装備略号／用語解説' not in item and '※新車時のカタログデータとなります。実際とは異なる場合がございますので、詳細は販売店にご確認ください。'not in item and 'カタログで車種情報を詳しく見る' not in item
                ]

                # TODO: title valueを分ける

                status_block_list.append(new_status_block)
            else:
                # status_list_html[3]以降が全てon offのやつ
                # -> :があった場合は区切るようにする。:以降は消す
                # -> これはそれぞれのstatusBlockで(on off4パターン)を頑張って切り分ける

                split_word = '：'
                status_block_title.append(status_block[0])
                li_list_res = status_block_html.find_all('li')
                li_html_list = []
                for li in li_list_res:
                    li_html_list.append(li)

                status_block_list.append(li_html_list)

        return status_block_list

    def my_index(self, l, x, default=False):
        if x in l:
            return l.index(x)
        else:
            return default

    def get_after_service_dict(self, bs_res: BeautifulSoup):
        # 補償の有無で判断(ダミー)、整備込みかどうか
        after_service_html = bs_res.find(
            'div', {'class': 'afterServiceBlock'}
        )
        after_service_list = after_service_html.find(
            'table').get_text().split()

        dummy_guarantee = 0
        if '保証付' in after_service_list[1]:
            dummy_guarantee = 1

        dummy_maintenance = 1
        if self.my_index(l=after_service_list, x='整備込') == False:
            dummy_maintenance = 0

        return {'補償': dummy_guarantee, '法定整備': dummy_maintenance}

    # class: qualityInnetTitle, qualityRank1, qualityRank2を取得
    # 1,2はtableの段の違いで、
    # 外装: qualityRank1[0], 内装: qualityRank1[1], 機関: qualityRank2[0], 修復歴: qualityRank2[1]
    def get_goo_kantei_hyouka_dict(self, bs_res: BeautifulSoup):
        goo_kantei_hyouka_html = bs_res.find(
            'div', {'class': 'gooKanteiHyoukaTable'}
        )

        quality_rank_1_list = goo_kantei_hyouka_html.find_all(
            'span', {'class': 'qualityRank1'}
        )
        quality_rank_1_list = [item.get_text() for item in quality_rank_1_list]

        quality_rank_2_list = goo_kantei_hyouka_html.find_all(
            'span', {'class': 'qualityRank2'}
        )
        quality_rank_2_list = [item.get_text() for item in quality_rank_2_list]

        return {'外装': quality_rank_1_list[0], '内装': quality_rank_1_list[1], '機関': quality_rank_2_list[0], '修復歴': quality_rank_2_list[1]}
