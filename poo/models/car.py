class Car:
    def __init__(self, id, license, driver, passengers):
        self.__id = id
        self.__license = license
        self.__driver = driver 
        self.__passengers = passengers

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_license(self):
        return self.__license

    def set_license(self, license):
        self.__license = license

    def get_driver(self):
        return self.__driver

    def set_driver(self, driver):
        self.__driver = driver

    def get_passengers(self):
        return self.__passengers

    def set_passengers(self, passengers):
        self.__passengers = passengers
