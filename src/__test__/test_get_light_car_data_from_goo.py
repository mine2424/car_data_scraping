import unittest
from src.services.scraping_data_service import ScrapingDataService


class TestGetLightCarFromGoo(unittest.TestCase):

    def test_get_car_grade(self):
        # ex) data: {'${car_name}': [{'year_text': 'yyyy年', 'url': 'xxx'}, ...] }
        data = {
            'あると': [{'year_text': '2020年', 'url': 'https://autos.goo.ne.jp/catalog/subaru/vivio/model/1997/'}]
        }
        result = ScrapingDataService.get_car_grade(self, car_list_by_year=data)
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
