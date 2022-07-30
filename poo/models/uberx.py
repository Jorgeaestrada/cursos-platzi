from models.car import Car


class UberX(Car):
    def __init__(self, id, license, driver, passengers, brand, model):
        super().__init__(id, license, driver, passengers)
        self.__brand = brand
        self.__model = model

    def get_id(self):
        return super().get_id()

    def set_id(self, id):
        super().set_id(id)

    def get_license(self):
        return super().get_license()

    def set_license(self, license):
        super().set_license(license)

    def get_driver(self):
        return super().get_driver()

    def set_driver(self, driver):
        super().set_driver(driver)

    def get_passengers(self):
        return super().get_passengers()

    def set_passengers(self, passengers):
        super().set_passengers(passengers)

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model