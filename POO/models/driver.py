from models.account import Account


class Driver(Account):
    def __init__(self, id, name, document, email, password):
        super().__init__(id, name, document, email, password)

    def get_id(self):
        return super().get_id()

    def set_id(self, id):
        super().set_name(id)

    def get_name(self):
        return super().get_name()

    def set_name(self, name):
        super().set_name(name)

    def get_document(self):
        return super().get_document()

    def set_document(self, document):
        super().set_document(document)

    def get_email(self):
        return super().get_email()

    def set_email(self, email):
        super().set_email(email)

    def get_password(self):
        return super().get_password()

    def set_password(self, password):
        super().set_password(password)

