from models.payment import Payments


class Card(Payments):
    def __init__(self, id, number, cvv, date):
        super.__init__(id)
        self.__number = number
        self.__cvv = cvv
        self.__date = date

    # overriding abstract method
    def charge(self, money):
        print(f'Se ha cobrado la cantidad de: ${self.money} mxn mediante Tarjeta VISA')
    
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_cvv(self):
        return self.__cvv

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    