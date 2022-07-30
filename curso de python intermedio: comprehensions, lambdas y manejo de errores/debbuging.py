def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input('Ingresa un numero:\n'))
            if num < 0:
                raise ValueError
            print('Divisores:   ', divisors(num))

        except ValueError as ve:
            print('Sólo se permiten números enteros positivos')
        print()

if __name__ == '__main__':
    run()