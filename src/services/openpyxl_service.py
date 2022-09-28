from openpyxl import Workbook
from openpyxl import load_workbook


from constants.openpyxl_constants import OpenPyxlConstants


class OpenpyxlService:
    def __init__(self) -> None:
        self.sheet = None
        self.book = None
        self.excelFile = ''
        self.max_col = 1
        self.max_row = 2

    def add_max_col(self):
        self.max_col += 1

    def add_max_row(self):
        self.max_row += 1

    def clear_max_col_row(self):
        self.max_col = 0
        self.max_row = 0

    def init_openpyxl(self, fileName: str):
        initializedSheet = Workbook()
        self.excelFile = f'../data/{fileName}.xlsx'
        initializedSheet.save(self.excelFile)
        self.book = load_workbook(self.excelFile)
        self.sheet = self.book.worksheets[0]
        return self.sheet

    def save_sheet(self, fileName: str = ''):
        if fileName == '':
            self.book.save(self.excelFile)
        else:
            self.book.save(filename=fileName)

    def create_title(self):
        for i, indexTitle in enumerate(OpenPyxlConstants.titles):
            self.sheet.cell(row=1, column=i+1).value = indexTitle
        self.save_sheet()

    def create_used_car_title(self):
        for i, indexTitle in enumerate(OpenPyxlConstants.used_car_titles):
            self.sheet.cell(row=1, column=i+1).value = indexTitle
        self.save_sheet()

    def add_data_in_sheet(self, light_car_detail_dict: dict):
        for i, light_car_detail in enumerate(light_car_detail_dict.values()):
            self.sheet.cell(
                row=self.max_row, column=i + 1
            ).value = light_car_detail

        self.add_max_row()
        self.save_sheet()

    def remove_space_col(self):
        self.sheet.delete_cols(5)
        self.save_sheet()
