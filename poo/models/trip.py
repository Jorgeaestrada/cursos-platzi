from models.car import Car
from models.driver import Driver
from models.payment import Payment
from models.route import Route


class Trip:
    def __init__(self, user):
        self.user = user
        # # la clase Trip se compone de estas otras clases (Composicion)

        self.car = Car()
        self.route = Route()
        self.payment = Payment()


    def make_trip(self):
        pass

    def get_car(self):
        return self.car

    def set_car(self, car):
        self.car = car

    def get_route(self):
        return self.car

    def set_route(self, route):
        self.route = route

    def get_payment(self):
        return self.car

    def set_payment(self, payment):
        self.payment = payment