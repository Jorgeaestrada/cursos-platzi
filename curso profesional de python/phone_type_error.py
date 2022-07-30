class Main:
    def __init__(self):
        self.FALLBACK_PHONE = '+e00000000'

    def get_phone(self):
        phone = input('Give me your phone:  ')
        if not phone:
						# 'str' object has no attribute 'round'
            return self.FALLBACK_PHONE.round()
        return int(phone)

    def run(self):
        my_phone = self.get_phone()
        print('Your phone is: {}'.format(my_phone))

if __name__ == '__main__':
    main = Main()
    main.run()