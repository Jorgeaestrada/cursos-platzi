from models.car import Car


class UberPool(Car):
    def __init__(self, id, license, driver, passengers):
        super().__init__(id, license, driver, passengers)

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model