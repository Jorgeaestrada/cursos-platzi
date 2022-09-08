def main():
    a = 1

    def nested():
        print(a)

    return nested


my_func = main()

# imprime 1 por el comportamiento del closure
my_func()
# eliminamos la funcion main con el keyword 'del'
del(main)
# imprime de nnuevo ya que la nested function es recordada
my_func()