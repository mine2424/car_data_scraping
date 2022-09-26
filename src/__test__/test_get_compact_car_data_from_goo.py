import unittest
from src.services.scraping_data_service import ScrapingDataService


class TestGetLightCarFromGoo(unittest.TestCase):

    # 実行コード
    # python3 -m unittest src/__test__/test_get_compact_car_data_from_goo.py
    def test_get_light_car_details(self):
        # ex) data: [{'年': year,'月': month,'メーカー': column_dict['car_maker'],'台数': '','通称名': car_name,'型番': new_car_details_value[3],'車種': '乗用','新車価格': new_car_details_value[0],'実質価格(CPI2007基準)': '','排気量': column_dict['displacement'],'トランスミッション': column_dict['driven'],'乗車定員': new_car_details_value[2],'ハイブリット': '','最高出力(kW)': new_car_details_value[11],'過給器': new_car_details_value[12],'燃費(WLTC)': new_car_details_value[13],'燃費(JC08)': new_car_details_value[13],'燃費(10.15)': new_car_details_value[13],'全長': all_length_list[0],'全幅': all_length_list[1],'全高': all_length_list[2],'サイズ': car_size,'車両重量': new_car_details_value[5],}]
        data = [
            {
                '３シリーズ': {
                    '20226': {'year_month': '20226', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10520000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10145014.html'},
                    '20224': {'year_month': '20224', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10260000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10143707.html'},
                    '20221': {'year_month': '20221', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｄ ｘＤｒｉｖｅツーリング Ｍスポーツ', 'displacement': '1995cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 6870000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10142055.html'},
                    '202112': {'year_month': '202112', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉエクスクルーシブ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 6070000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10141348.html'},
                    '20214': {'year_month': '20214', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10250000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10137103.html'},
                    '20209': {'year_month': '20209', 'car_maker': 'ＢＭＷ', 'grade_name': '３１８ｉツーリング Ｍスポーツ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 5840000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10133623.html'},
                    '20208': {'year_month': '20208', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10120000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10134734.html'},
                    '20205': {'year_month': '20205', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｄ ｘＤｒｉｖｅツーリング Ｍスポーツ', 'displacement': '1995cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 6740000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10133504.html'},
                    '20204': {'year_month': '20204', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10100000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10131676.html'},
                    '20203': {'year_month': '20203', 'car_maker': 'ＢＭＷ', 'grade_name': '３３０ｅ Ｍスポーツ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 6670000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10128965.html'},
                    '201911': {'year_month': '201911', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅツーリング', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 10050000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10127588.html'},
                    '201910': {'year_month': '201910', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅ', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 9800000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10125738.html'},
                    '20195': {'year_month': '20195', 'car_maker': 'ＢＭＷ', 'grade_name': 'Ｍ３４０ｉ ｘＤｒｉｖｅ', 'displacement': '2997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 9620000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10123719.html'},
                    '20193': {'year_month': '20193', 'car_maker': 'ＢＭＷ', 'grade_name': '３３０ｉ Ｍスポーツ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 6320000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10120083.html'},
                    '20191': {'year_month': '20191', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング Ｍスポーツ', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8750000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10120041.html'},
                    '20181': {'year_month': '20181', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング Ｍスポーツ', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8720000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10114786.html'}, '20178': {'year_month': '20178', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング Ｍスポーツ', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8540000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10112679.html'}, '20176': {'year_month': '20176', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング ラグジュアリー', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8350000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10111833.html'}, '20175': {'year_month': '20175', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｄ ｘＤｒｉｖｅ グランツーリスモ Ｍスポーツ', 'displacement': '1995cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 7060000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10109817.html'}, '20174': {'year_month': '20174', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉグランツーリスモ Ｍスポーツ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 6510000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10116724.html'}, '201610': {'year_month': '201610', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング ラグジュアリー', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8350000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10108163.html'}, '20165': {'year_month': '20165', 'car_maker': 'ＢＭＷ', 'grade_name': '３４０ｉツーリング ラグジュアリー', 'displacement': '2997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8040000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10104442.html'}, '20161': {'year_month': '20161', 'car_maker': 'ＢＭＷ', 'grade_name': '３３０ｅ Ｍスポーツ', 'displacement': '1998cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 5990000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10102077.html'},
                    '20159': {'year_month': '20159', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉグランツーリスモ ラグジュアリー', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8150000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10101655.html'},
                    '201411': {'year_month': '201411', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉグランツーリスモ Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8110000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10094403.html'},
                    '201410': {'year_month': '201410', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉツーリング ＳＥ', 'displacement': '1997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 4490000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10094431.html'},
                    '20148': {'year_month': '20148', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉツーリング Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 7960000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10093086.html'},
                    '20144': {'year_month': '20144', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉグランツーリスモ Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 8050000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10089490.html'},
                    '20141': {'year_month': '20141', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｄツーリング Ｍスポーツ', 'displacement': '1995cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 5470000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10086893.html'},
                    '20138': {'year_month': '20138', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉグランツーリスモ Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 7760000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10084846.html'}, '20136': {'year_month': '20136', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉグランツーリスモ スポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 7500000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10083169.html'}, '20134': {'year_month': '20134', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉツーリング Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 7550000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10082579.html'}, '201212': {'year_month': '201212', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉツーリング Ｍスポーツ', 'displacement': '1997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 5150000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10081004.html'}, '20129': {'year_month': '20129', 'car_maker': 'ＢＭＷ', 'grade_name': '３２８ｉツーリング Ｍスポーツ', 'displacement': '1997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 6320000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10078429.html'}, '20128': {'year_month': '20128', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉ ｘＤｒｉｖｅ Ｍスポーツ', 'displacement': '1997cc', 'driven': 'FULL4WD', 'fuel_consumption': '－', 'price': 5240000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10080343.html'}, '20127': {'year_month': '20127', 'car_maker': 'ＢＭＷ', 'grade_name': 'アクティブハイブリッド３ Ｍスポーツ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 7450000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10077620.html'}, '20124': {'year_month': '20124', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉ スポーツ', 'displacement': '1997cc', 'driven': 'FR', 'fuel_consumption': '－', 'price': 4700000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10075483.html'}, '20121': {'year_month': '20121', 'car_maker': 'ＢＭＷ', 'grade_name': '３２８ｉスポーツ', 'displacement': '1997cc', 'driven': 'FR', 'fuel_consumption': '15.6km/l', 'price': 5860000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10074265.html'}, '201110': {'year_month': '201110', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '10.6km/l', 'price': 8150000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10073670.html'}, '20105': {'year_month': '20105', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '10.6km/l', 'price': 8150000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10062275.html'}, '200910': {'year_month': '200910', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉツーリング スタイル・エッセンス', 'displacement': '1995cc', 'driven': 'FR', 'fuel_consumption': '11.4km/l', 'price': 4240000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10058546.html'}, '200812': {'year_month': '200812', 'car_maker': 'ＢＭＷ', 'grade_name': '３２５ｉ ｘＤｒｉｖｅ', 'displacement': '2496cc', 'driven': 'FULL4WD', 'fuel_consumption': '9.3km/l', 'price': 5680000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10053061.html'}, '200811': {'year_month': '200811', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '8.9km/l', 'price': 8020000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10052143.html'}, '200810': {'year_month': '200810', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '8.7km/l', 'price': 7950000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10051024.html'}, '20085': {'year_month': '20085', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉ', 'displacement': '1995cc', 'driven': 'FR', 'fuel_consumption': '12.0km/l', 'price': 4160000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10047441.html'}, '20081': {'year_month': '20081', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '8.7km/l', 'price': 7880000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10045322.html'}, '200711': {'year_month': '200711', 'car_maker': 'ＢＭＷ', 'grade_name': '３２５ｘｉ', 'displacement': '2496cc', 'driven': 'FULL4WD', 'fuel_consumption': '9.3km/l', 'price': 5650000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10044401.html'}, '20075': {'year_month': '20075', 'car_maker': 'ＢＭＷ', 'grade_name': '３２３ｉ', 'displacement': '2496cc', 'driven': 'FR', 'fuel_consumption': '9.9km/l', 'price': 4870000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10040813.html'}, '20072': {'year_month': '20072', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉカブリオレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '8.7km/l', 'price': 7830000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10038764.html'}, '200610': {'year_month': '200610', 'car_maker': 'ＢＭＷ', 'grade_name': '３３５ｉツーリング', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '8.6km/l', 'price': 6880000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10036742.html'}, '20069': {'year_month': '20069', 'car_maker': 'ＢＭＷ', 'grade_name': '３３０Ｃｉカブリオーレ', 'displacement': '2979cc', 'driven': 'FR', 'fuel_consumption': '9.2km/l', 'price': 7320000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10035224.html'}, '20065': {'year_month': '20065', 'car_maker': 'ＢＭＷ', 'grade_name': '３２０ｉツーリング', 'displacement': '1995cc', 'driven': 'FR', 'fuel_consumption': '11.4km/l', 'price': 4370000, 'url': 'https://autos.goo.ne.jp/catalog/detail/10033743.html'},
                }
            }
        ]
        result = ScrapingDataService.get_light_car_details(
            self, grade_list_by_all_year=data
        )
        assert result is not None

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()