#funciones aritmeticas de una vez :D
def suma(a,b):
    return (a+b)

def resta(a,b):
    return (a-b)

def multip(a,b):
    return (a*b)

def divis(a,b):
    return (a/b)

def modul(a,b):
    return (a%b)

#se añade nueva función para la ultima practica
def exponent(a,b):
    return (a**b)

#funcion auxiliar que se me ocurrió para validar la entrada de numeros porque tengo mucho tiempo todavia
def pedirNum(valor):
    while True:
        try:
            return float(input(valor))
        except ValueError:
            print("Error. Entrada no valida, introduzca solo numeros enteros o decimales.\n\n")



def calculadora():
    print("====CALCULADORA MAS BASICA DEL MUNDO====\n")
    print("Por favor, no pida mucho que la hice en 30min y a parte usando Vim porque me gusta batallar\n")
    print("======================================================")

    #creo un acumulador para ir guardando el resultado
    resultado = pedirNum("Introduce un valor por favor: ")


    #bucle infinito para que pida siempre un valor hasta que no lo rompa el usuario
    while True:
        operador = input("OPERADORES: '+' para sumar, '-' para restar, '*' para multiplicar, '/' para dividir, '%' para modulo,'**' para potencias, o '=' para obtener resultado. \n Introduzca operación: ")


        if operador == '=':
            break

        #validamos la entrada
        if operador not in ('+','-','*','/','%','**'):
            print("Operación desconocida, por favor, intente de nuevo\n\n")
            continue

        siguienteNum = pedirNum("Introduce el siguiente valor: ")

        #aplicamos la logica aritmetica y de control que se ocupa
        if operador == '+':
            resultado = suma(resultado, siguienteNum)

        elif operador == '-':
            resultado = resta(resultado, siguienteNum)

        elif operador == '*':
            resultado = multip(resultado, siguienteNum)

        elif operador == '/':
            if siguienteNum == 0:
                print("Error. No se puede dividir entre cero.\n\n")
                continue

            resultado = divis(resultado, siguienteNum)

        elif operador == '%':
            resultado = modul(resultado, siguienteNum)

        elif operador == '**':
            resultado = exponent(resultado, siguienteNum)

        print(f"Subtotal actual: {resultado}\n\n")

    print(f"\nResultado final: {resultado}\n")
    print("GRACIAS POR PROBAR MI CALCULADORA CHAFA ;D\n\n\n")
    


#arrancamos la funcion calculadora
calculadora()
    
