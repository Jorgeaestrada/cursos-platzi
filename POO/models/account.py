class Account:
    def __init__(self, id, name, document, email, password):
        self.__id = id
        self.__name = name
        self.__document = document
        self.__email = email
        self.__password = password

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_document(self):
        return self.__document

    def set_document(self, document):
        self.__document = document

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password