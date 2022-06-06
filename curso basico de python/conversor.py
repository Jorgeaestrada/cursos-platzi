from time import sleep

# ARS = argentinos, COP = colombianos, MXN = mexicanos
tipo_de_cambio = [["ARS", 113.79], ["COP", 3724.45], ["MXN", 19.99]]

while True:
    print("bienvenido al conversor de monedas\n")
    print("1. Pesos Colombianos")
    print("2. Pesos Argentinos")
    print("3. Pesos Mexicanos")
    print("4. Salir\n")
    opcion = int(input("elige una opcion:   "))

    if opcion == 1:
        pesos = input("\n¿Cuántos pesos argentinos tienes?:    ")
    elif opcion == 2:
        pesos = input("\n¿Cuántos pesos colombianos tienes?:    ")
    elif opcion == 3:
        pesos = input("\n¿Cuántos pesos mexicanos tienes?:    ")
    elif opcion == 4:
        break
    else:
        print("elige una opción válida para continuar. . .\n")
        sleep(3)

    dolares = float(pesos) / tipo_de_cambio[opcion - 1][1]
    dolares = str(round(dolares, 2))
    print("\nTienes ${} dólares\n".format(dolares))
    sleep(3)    
