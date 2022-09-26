import random
from urllib import request
from bs4 import BeautifulSoup


class ScrapingUsedCarDataService:
    def __init__(self) -> None:
        pass

    random_seconds = random.uniform(0.234, 1.000)

    def init_BeautifulSoup(self, url: str):
        res = request.get(url)
        res.encoding = res.apparent_encoding
        return BeautifulSoup(res.text, 'html.parser')

    def get_used_car_overview(self):
        self.init_BeautifulSoup(self, url='')
