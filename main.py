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

def calculadora():
    print("====CALCULADORA MAS BASICA DEL MUNDO====\n")
    print("Por favor, no pida mucho que la hice en 30min y a parte usando Vim porque me gusta batallar\n")
    print("======================================================")

    #creo un acumulador para ir guardando el resultado
    resultado = float(input("Introduce un valor por favor: "))


    #bucle infinito para que pida siempre un valor hasta que no lo rompa el usuario
    while True:
        operador = input("OPERADORES: '+' para sumar, '-' para restar, '*' para multiplicar, '/' para dividir, '%' para modulo, o '=' para obtener resultado. \n Introduzca operación: ")


        if operador == '=':
            break

        #validamos la entrada
        if operador not in ('+','-','*','/','%'):
            print("Operación desconocida, por favor, intente de nuevo\n\n")
            continue

        siguienteNum = float(input("Introduce el siguiente valor: "))

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

        print(f"Subtotal actual: {resultado}\n\n")

    print(f"\nResultado final: {resultado}\n")
    print("GRACIAS POR PROBAR MI CALCULADORA CHAFA ;D\n\n\n")
    


#arrancamos la funcion calculadora
calculadora()
    
