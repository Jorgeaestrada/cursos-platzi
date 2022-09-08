""" Versión iterativa de la 
sucesion de fibonacci """


def fibonacci(n):
    a = 0
    b = 1

    # para k desde 0 hasta n
    for _ in range(0, n):
        c = b + a
        a = b
        b = c
        print(a)


fibonacci(3)
