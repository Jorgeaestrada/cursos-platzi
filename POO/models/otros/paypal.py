from models.payment import Payment


class PayPal(Payment):
    def __init__(self, id, email):
        super.__init__(id)
        self.__email = email

    # overriding abstract method
    def charge(self, money):
        print(f'Se ha cobrado la cantidad de: ${self.money} mxn mediante PAYPAL')
    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email