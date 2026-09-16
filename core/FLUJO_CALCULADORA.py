from core import VALIDADOR_NUMERICO
from core import LIBRERIA_ARITMETICA

def calculadora():
    print("====CALCULADORA MAS BASICA DEL MUNDO====\n")
    print("======================================================")

    #creo un acumulador para ir guardando el resultado
    resultado = VALIDADOR_NUMERICO.pedirNum("Introduce un valor por favor: ")

    salir = False

    #bucle controlado mediante variable booleana. Decidí cambiar el while true
    while not salir:
        operador = input("OPERADORES: '+' para sumar, '-' para restar, '*' para multiplicar, '/' para dividir, '%' para modulo,'**' para potencias, o '=' para obtener resultado. \n Introduzca operación: ")

        if operador == '=':
            print(f"\nResultado final: {resultado}\n")
            print("GRACIAS POR PROBAR MI CALCULADORA ;D\n\n")
            salir = True
            continue
            
        
        if operador not in ('+', '-', '*', '/', '%', '**'):
            print("Operación desconocida, por favor, intente de nuevo\n\n")
            continue
        
        siguienteNum = VALIDADOR_NUMERICO.pedirNum("Introduce el siguiente valor: ")

        match operador:
            
        #aplicamos la logica aritmetica y de control que se ocupa
            case '+':
                resultado = LIBRERIA_ARITMETICA.suma(resultado, siguienteNum)

            case '-':
                resultado = LIBRERIA_ARITMETICA.resta(resultado, siguienteNum)

            case '*':
                resultado = LIBRERIA_ARITMETICA.multip(resultado, siguienteNum)

            case '/':
                if siguienteNum == 0:
                    print("Error bebé, no se puede dividir entre cero.\n\n")
                    continue

                resultado = LIBRERIA_ARITMETICA.divis(resultado, siguienteNum)

            case '%':
                resultado = LIBRERIA_ARITMETICA.modul(resultado, siguienteNum)

            case '**':
                resultado = LIBRERIA_ARITMETICA.potencia(resultado, siguienteNum)


        print(f"Subtotal actual: {resultado}\n\n")


    