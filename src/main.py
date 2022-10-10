# test only
# from src.constants.openpyxl_constants import OpenPyxlConstants
# from src.services.scraping_data_service import ScrapingDataService
# from src.services.openpyxl_service import OpenpyxlService

from constants.openpyxl_constants import OpenPyxlConstants
from services.scraping_data_service import ScrapingDataService
from services.openpyxl_service import OpenpyxlService

from tqdm import tqdm
import time
import random
import sys
from concurrent.futures import ThreadPoolExecutor


from services.scraping_used_car_data_service import ScrapingUsedCarDataService

print('this is goo car scraping!!!')


def main():
    argv = int(sys.argv[1])
    if argv == 0:
        run_scraping_all_light_car_catalog_data()
    elif argv == 1:
        run_scraping_all_used_light_car_data()
    elif argv == 2:
        judge_cell_color()
    elif argv == 3:
        insert_model_and_maker_in_used()


def run_scraping_all_light_car_catalog_data():
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

    # input excel name #
    # openpyxl_service.init_openpyxl(fileName='all_light_car_data_by_all_grade')
    openpyxl_service.init_openpyxl(
        fileName='all_light_rv_car_data_by_all_grade'
    )
    #
    # openpyxl_service.init_openpyxl(fileName='all_filled_light_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_light_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_light_car_data_by_min')
    # openpyxl_service.init_openpyxl(fileName='all_light_rv_car_data_by_min')
    # openpyxl_service.init_openpyxl(fileName='all_light_rv_car_data_by_max_2')
    #
    # openpyxl_service.init_openpyxl(fileName='all_compact_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_minivan_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_sedan_car_data_by_max')
    # openpyxl_service.init_openpyxl(fileName='all_coupe_car_data_by_max')

    openpyxl_service.create_title()

    pre_month = 0
    pre_year = 0
    pre_car_name = ''
    for i, car_detail in enumerate(tqdm(all_light_car_details)):
        time.sleep(random_seconds)

        month = int(car_detail['月'])
        year = int(car_detail['年'])

        # 埋めない場合はこれだけコメントアウトを外す
        openpyxl_service.add_data_in_sheet(
            light_car_detail_dict=car_detail
        )

        # 年月を全て埋め合わせる処理 #

        # print(f'car_detail: {car_detail}')
        # if (pre_year == 0 and pre_month == 0) or car_detail['通称名'] != pre_car_name:
        #     openpyxl_service.add_data_in_sheet(
        #         light_car_detail_dict=car_detail
        #     )
        # else:
        #     if year == pre_year:
        #         # 比較して同年なら
        #         diff = abs(month - pre_month) + 1
        #         print('diff', diff)
        #         print(f'month: {month}, pre_month: {pre_month}')
        #         if diff > 0:
        #             for i in range(diff):
        #                 car_detail['月'] = month+i
        #                 openpyxl_service.add_data_in_sheet(
        #                     light_car_detail_dict=car_detail
        #                 )
        #         else:
        #             openpyxl_service.add_data_in_sheet(
        #                 light_car_detail_dict=car_detail
        #             )
        #     else:
        #         # 比較して別年なら
        #         pre_diff = abs(12-pre_month) + 1
        #         pro_diff = month+1
        #         print(f'pre_diff: {pre_diff}, pro_diff: {pro_diff}')
        #         print(f'month: {month}, pre_month: {pre_month}')

        #         # 前年度
        #         if pre_diff > 0:
        #             for i in range(pre_diff):
        #                 car_detail['月'] = month + i
        #                 openpyxl_service.add_data_in_sheet(
        #                     light_car_detail_dict=car_detail
        #                 )
        #         else:
        #             openpyxl_service.add_data_in_sheet(
        #                 light_car_detail_dict=car_detail
        #             )

        #         # 今年度
        #         if pro_diff > 0:
        #             for i in range(pro_diff):
        #                 car_detail['年'] = year
        #                 car_detail['月'] = month + i
        #                 openpyxl_service.add_data_in_sheet(
        #                     light_car_detail_dict=car_detail
        #                 )
        #         else:
        #             openpyxl_service.add_data_in_sheet(
        #                 light_car_detail_dict=car_detail
        #             )

        # pre_year = year
        # pre_month = month
        # pre_car_name = car_detail['通称名']
        # print(' ')
        # print(' ')

        # 年月を全て埋め合わせる処理 end #

    print(f'all data wrote csv')


def run_scraping_all_used_light_car_data():
    scraping_data_service = ScrapingUsedCarDataService()
    openpyxl_service = OpenpyxlService()

    ### 中古車のURLを取得する ###
    # output: detail_page_url_list
    detail_page_url_list = scraping_data_service.get_all_used_car_overview_url_list(
        url='https://www.goo-net.com/usedcar/bodytype-KEI/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_WAGON/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_CUSTOM/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_X/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPACE/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPACE_CUSTOM/'
        # url='https://www.goo-net.com/usedcar/brand-MITSUBISHI/car-EK_SPORT/'
    )

    print('length', len(detail_page_url_list))

    ### 詳細ページのデータを取得 ###

    all_detail_page_data = []
    for i, detail_page_url in enumerate(tqdm(detail_page_url_list)):
        # if i < 3:
        random_seconds = random.uniform(0.001, 0.01)
        time.sleep(random_seconds)
        detail_page_data = scraping_data_service.get_detail_page_data(
            detail_url=detail_page_url
        )
        all_detail_page_data.append(detail_page_data)

    ### excelに書き込む ###

    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_wagon')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_custom')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_custom_test')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_x')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_space')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_space_custom')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_space')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_x_space')
    # openpyxl_service.init_openpyxl(fileName='all_used_car_data_by_ek_sport')
    openpyxl_service.init_openpyxl(fileName='used_light_car_1000')

    openpyxl_service.create_used_car_title()

    for car_detail in tqdm(all_detail_page_data):
        openpyxl_service.add_used_car_data_in_sheet(
            val_list=car_detail
        )


def judge_cell_color():
    openpyxl_service = OpenpyxlService()

    sheet = openpyxl_service.openpyxl(
        'f_all_light_rv_car_data_by_all_grade', 1
    )

    index_list = openpyxl_service.get_colored_cell_index_list()
    openpyxl_service.get_max_row()
    max_row = openpyxl_service.max_row
    sheet.cell(row=1, column=28).value = 'price_median'

    is_colored = False
    for row in range(max_row):
        row = row + 2
        for idx in index_list:
            if idx == row:
                print('row colored', row)
                openpyxl_service.add_data_in_exit_file(28, row, 1)
                is_colored = True

        if is_colored == False:
            print('row not colored', row)
            openpyxl_service.add_data_in_exit_file(28, row, 0)

        is_colored = False


def add_model_maker_in_excel(instance, i: int, model_and_maker):
    instance.add_data_in_exit_file(
        1, i, model_and_maker['maker']
    )
    instance.add_data_in_exit_file(
        2, i, model_and_maker['model']
    )


def insert_model_and_maker_in_used():
    openpyxlServiceinstance = OpenpyxlService()

    # 新しく作成していくall_used_car_final(edit)_2的な？
    sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_2', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_3', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_4', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_5', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_6', 0)
    # sheet = openpyxlServiceinstance.openpyxl('all_used_car_final(edit)_7', 0)

    rows = sheet.rows
    max_column = sheet.max_column
    scraping_instance = ScrapingUsedCarDataService()

    # TODO: rowsを切り分けて、複数処理をする
    # rows = list(rows)
    rows = list(rows)[0:5000]
    # rows = list(rows)[5001:10000]
    # rows = list(rows)[10001:15000]
    # rows = list(rows)[15001:20000]
    # rows = list(rows)[20001:25000]
    # rows = list(rows)[25001:30000]
    # rows = list(rows)[30001:33347]

    model_and_maker_list = scraping_instance.get_model_and_maker(rows)

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i, model_and_maker in enumerate(tqdm(model_and_maker_list)):
            i = i + 2

            # 2~ページはindexを追加すること
            # TODO: 検証を必ずする（テストデータで）
            # i = i + 5001

            executor.submit(
                add_model_maker_in_excel, openpyxlServiceinstance, i, model_and_maker
            )


if __name__ == '__main__':
    main()
