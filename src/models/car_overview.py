class CarOverview:
    def __init__(self) -> None:
        self.url
        self.car_name
        self.car_maker

    def copyWith(self, url, car_name, car_maker):
        if not url and not self.url:
            self.url = ''
        else:
            self.url = url
        if not car_name and not self.car_name:
            self.car_name = ''
        else:
            self.car_name = car_name
        if not car_maker and not self.car_maker:
            self.car_maker = ''
        else:
            self.car_maker = car_maker
