from constants.openpyxl_constants import OpenPyxlConstants
from services.scraping_data_service import ScrapingDataService
from services.openpyxl_service import OpenpyxlService
from tqdm import tqdm
import concurrent.futures
import time
import random
import numpy as np
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

    # data: [{'年': year,'月': month,'メーカー': column_dict['car_maker'],'台数': '','通称名': car_name,'型番': new_car_details_value[3],'車種': '乗用','新車価格': new_car_details_value[0],'実質価格(CPI2007基準)': '','排気量': column_dict['displacement'],'トランスミッション': column_dict['driven'],'乗車定員': new_car_details_value[2],'ハイブリット': '','最高出力(kW)': new_car_details_value[11],'過給器': new_car_details_value[12],'燃費(WLTC)': new_car_details_value[13],'燃費(JC08)': new_car_details_value[13],'燃費(10.15)': new_car_details_value[13],'全長': all_length_list[0],'全幅': all_length_list[1],'全高': all_length_list[2],'サイズ': car_size,'車両重量': new_car_details_value[5],}]
    all_light_car_details = scraping_data_service.get_light_car_details(
        grade_list_by_all_year=all_car_grade
    )

    ### csvに出力する実装 ###

    random_seconds = random.uniform(0.234, 1.000)
    # openpyxl_service.init_openpyxl(fileName='all_light_car_data_by_median')
    # openpyxl_service.init_openpyxl(fileName='all_light_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_light_rv_car_data_by_max')
    openpyxl_service.init_openpyxl(fileName='all_light_rv_car_data_by_median')

    openpyxl_service.create_title()

    pre_year_month = 0
    current_month_index = 12
    for i, car_detail in enumerate(tqdm(all_light_car_details)):
        time.sleep(random_seconds)
        # TODO: 不足分の年月を追加する
        year_month = int(car_detail['年']+car_detail['月'])
        diff_year_month = year_month
        if pre_year_month != 0:
            diff_year_month = year_month - pre_year_month

        # 年の比較をする
        if diff_year_month != 1:
            if pre_year_month == 0:
                init_diff = int(car_detail['月'])+1
                # 月をインクリメントする
                for i in range(init_diff):
                    car_detail['月'] = current_month_index
                    openpyxl_service.add_data_in_sheet(
                        light_car_detail_dict=car_detail
                    )
                    if current_month_index == 1:
                        current_month_index = 12
                    else:
                        current_month_index = current_month_index - 1
            else:
                # 年を跨ぐかどうかを判別する
                if str(pre_year_month)[:4] != str(year_month)[:4]:
                    pre_diff = 12-(int(pre_year_month[4:])+1)
                    cur_diff = int(year_month[4:])+1
                    for i in range(pre_diff):
                        car_detail['月'] = current_month_index
                        openpyxl_service.add_data_in_sheet(
                            light_car_detail_dict=car_detail
                        )
                        if current_month_index == 1:
                            current_month_index = 12
                        else:
                            current_month_index = current_month_index - 1

                    for j in range(cur_diff):
                        car_detail['月'] = current_month_index
                        openpyxl_service.add_data_in_sheet(
                            light_car_detail_dict=car_detail
                        )
                        if current_month_index == 1:
                            current_month_index = 12
                        else:
                            current_month_index = current_month_index - 1

                    # TODO: preの年の差分(12-preの月)とyear_monthの差分(range(1,year_monthの月))を回す
                else:
                    for i in range(pre_year_month, pre_year_month+diff_year_month):
                        # 年月をインクリメントする
                        car_detail['月'] = current_month_index
                        openpyxl_service.add_data_in_sheet(
                            light_car_detail_dict=car_detail
                        )
                        if current_month_index == 1:
                            current_month_index = 12
                        else:
                            current_month_index = current_month_index - 1
        else:
            openpyxl_service.add_data_in_sheet(
                light_car_detail_dict=car_detail
            )

            if current_month_index == 1:
                current_month_index = 12
            else:
                current_month_index = current_month_index - 1

    print(f'all data wrote csv')


if __name__ == '__main__':
    main()
