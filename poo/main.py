from models.cash import Cash
from models.driver import Driver
from models.route import Route
from models.trip import Trip
from models.uberx import UberX
from models.user import User

if __name__ == '__main__':
    # creamos el objeto User que HEREDA de la clase Account
    user = User(1, 'Anahí Salgado', 'user_doc', 'anahi.salgado@email.com', 'u53r_53cr3t')

    # creamos el objeto Driver que HEREDA de la clase Account
    driver = Driver(1, 'jorge.estrada', 'driver_doc', 'jorge.estrada@email.com', 'dr1v3r_53cr37')

    # creamos el objeto UberX que HEREDA de la clase Car y tiene un Driver
    car = UberX(1, 'L1C-M3X', driver, 3, 'Audi', 'A5 sportback')
    # creamos el objeto Route
    route = Route('Casa', 'Trabajo', 2000) 
    # creamos el objeto Cash que HEREDA de la clase Payment
    payment = Cash(1, 'anahi.salgado@email.com')

    # creamos el objeto Trip el cual tiene un Usuario
    trip = Trip(user)
    # composicion
    trip.set_car(car)
    trip.set_route(route)
    trip.set_payment(payment)
