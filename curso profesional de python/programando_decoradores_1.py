from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        time_elapsed = str(time_elapsed.total_seconds())
        print("Pasaron: {} segundos".format(time_elapsed))

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Jorge Estrada"):
    print("Hola {}".format(nombre))


def run():
    random_func()
    suma(5, 5)
    saludo()


if __name__ == "__main__":
    run()