#funcion auxiliar que se me ocurrió para validar la entrada de numeros porque tengo mucho tiempo todavia
def pedirNum(valor):
    while True:
        try:
            return float(input(valor))
        except ValueError:
            print("Error. Entrada no valida, introduzca solo numeros enteros o decimales.\n\n")
