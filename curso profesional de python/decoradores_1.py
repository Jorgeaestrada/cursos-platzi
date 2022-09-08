def decorador(func):
    def envoltura():
        print('Esto se añade a una función original')
        func()
    return envoltura


def saludo():
    print('¡Hola!')


saludo()

saludo = decorador(saludo)
saludo()
