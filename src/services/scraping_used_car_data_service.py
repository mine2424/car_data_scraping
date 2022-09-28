from math import floor
import random
import time
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
        #
        # url -> 'https://www.goo-net.com/usedcar/bodytype-KEI/'
        count_html = bs_res.find_all('span', {'class': 'count'})[0]
        all_count = int(
            count_html.get_text().replace(',', '')
        )
        overview_url_list = [url]

        # 本番用
        # overview_url_length = floor(all_count / 50)

        # テスト用
        overview_url_length = 1

        for i in range(overview_url_length):
            url_index = i + 2

            # 全軽自動車取得用
            # current_url = f'https://www.goo-net.com/usedcar/bodytype-KEI/index-{url_index}.html'

            # brand-MITSUBISHI/car-EK_WAGON only
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

        # print('detail_page_url_list', detail_page_url_list)
        return detail_page_url_list

    def get_detail_page_data(self, detail_url: str):
        bs_res = ScrapingUsedCarDataService.init_BeautifulSoup(
            self, url=detail_url
        )

        # TODO: 仮になかったらの処理を書く
        # TODO: tag: table, class: mainDataで価格を取得
        # TODO: tag: div, class: statusBlockで車両詳細を取得
        # TODO: tag: div, class: afterServiceBlockでアフターサービスを取得
        # TODO: tag: div, class: gooKanteiHyoukaTableでgoo鑑定を取得

        price_html = bs_res.find('table', {'class': 'mainData'})
        status_list_html = bs_res.find_all('div', {'class': 'statusBlock'})
        after_service_html = bs_res.find_all(
            'div', {'class': 'afterServiceBlock'}
        )
        goo_kantei_hyouka_html = bs_res.find_all(
            'div', {'class': 'gooKanteiHyoukaTable'}
        )

        print('price_html', price_html.get_text().split())
        # print('status_list_html', status_list_html)
        # print('after_service_html', after_service_html)
        # print('goo_kantei_hyouka_html', goo_kantei_hyouka_html)
        print(' ')
        print(' ')
