from constants.openpyxl_constants import OpenPyxlConstants
from services.scraping_data_service import ScrapingDataService
from services.openpyxl_service import OpenpyxlService
from tqdm import tqdm
import concurrent.futures
import time
import random
print('this is goo car scraping!!!')


def main():
    scraping_data_service = ScrapingDataService()
    openpyxl_service = OpenpyxlService()
    openpyxl_constants = OpenPyxlConstants()

    ### スクレイピングしてデータを取得する実装 ###

    # data: [{'url': url, 'car_name': title, 'car_maker': manufacturer}]
    all_light_ca_overview = scraping_data_service.get_all_light_car_overview()

    # data: {'${car_name}': [{'year_text': 'yyyy年', 'car_maker': manufacturer, 'url': 'xxx'}, ...] }
    all_light_car_by_year = scraping_data_service.get_all_light_car_by_year(
        car_overview_list=all_light_ca_overview
    )

    # data: [
    #           {
    #               'car_name': {
    #                   'year_month': {
    #                       'year_month': 202209, 'grade_name': 'Ｘ', 'displacement': '658cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 1290300, 'url': 'xxx'
    #                    },
    #                    ...
    #                },
    #                ...
    #           },
    #           ...
    # ]
    all_car_grade = scraping_data_service.get_car_grade(
        car_list_by_year=all_light_car_by_year
    )

    all_light_car_details = scraping_data_service.get_light_car_details(
        grade_list_by_all_year=all_car_grade
    )
    print('all_light_car_details', all_light_car_details)

    ### csvに出力する実装 ###

    random_seconds = random.uniform(0.234, 1.000)
    openpyxl_service.init_openpyxl(fileName='all_light_car_data')

    openpyxl_service.create_title()

    for i, car_detail in enumerate(tqdm(all_light_car_details)):
        openpyxl_service.add_data_in_sheet(light_car_detail_dict=car_detail)

    print(f'all data wrote csv')


if __name__ == '__main__':
    main()
