from models.car import Car


class UberBlack(Car):   

    type_car_accepted = []
    seats_material = []

    def __init__(self, id, license, driver, passengers, type_car_accepted, seats_material):
        super().__init__(id, license, driver, passengers)
        self.__type_car_accepted = type_car_accepted
        self.__seats_material = seats_material

    def get_type_car_accepted(self):
        return self.__type_car_accepted

    def set_type_car_accepted(self, type_car_accepted):
        self.__type_car_accepted = type_car_accepted

    def get_seats_material(self):
        return self.__seats_material

    def set_seats_material(self, seats_material):
        self.__seats_material = seats_material