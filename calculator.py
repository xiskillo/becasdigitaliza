
"""
Realizar el código de la calculadora y subirlo a vuestra cuenta de GitHub: 

-Crear un archivo llamado calculator.py
-Crear las sentencias necesarias para recoger dos números a través del terminal
-Integrar funcionalidades de suma, resta, multiplicación, división, y exponencial
-Implementar funciones, diccionarios, y excepciones
-Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
-Realizar las operaciones e imprimir el valor por pantalla.
-Subir el archivo a vuestra cuenta de GitHub.
"""
import sys

print ("BIENVENIDO A LA CALCULADORA CON PYTHON, POR FRANCISCO JOSÉ ACASO VALVERDE\n")

menu={"Opción 1":"Para SUMAR, pulse 1",
    "Opción 2":"Para RESTAR, pulse 2",
    "Opción 3":"Para MULTIPLICAR, pulse 3",
    "Opción 4":"Para DIVIDIR, pulse 4",
    "Opción 5":"Para EXPONENCIAL, pulse 5",
    "Opción 6":"Para SALIR, pulse 6"}




while (True):

    try:
        for i, x in menu.items():
            print (i,"--->",x)
        opcion=int(input("Introduce la opción deseada:\n"))
    except ValueError:
        print ("Has introducido elementos inválidos..")
    

    def introduccion():
        while (True):
                try:
                    a=input("Introduzca la primera cifra: ")
                    b=input("Introduzca la segunda cifra: ")


                    y=list(a)
                    z=list(b)

                    for i in range(len(y)):
                        if y[i]==',':
                            y[i]='.'

                    for i in range(len(z)):
                        if z[i]==',':
                            z[i]='.'
                
                    
                    a=float("".join(y))
                    b=float("".join(z))

                    
                    
                    return a,b
                    break
                    
                    

                except (TypeError, ValueError):
                    print ("Escribe solamente cifras, con puntos o comas, nunca letras. Escribe otra vez: \n")



   


    def sumar():
        print ("La suma de {} y {} es: ".format(a,b),a+b)


    def restar():
        print ("La resta de {} y {} es: ".format(a,b),a-b)


    def multiplicar():
        print ("La multiplicacion de {} y {} es: ".format(a,b),a*b)
        


    def dividir():
        print ("La division de {} y {} es: ".format(a,b),a/b)


    def exponencial():
        print ("El número {} elevado a {} es: ".format(a,b),a**b)

    def salir():
        print ("¡ADIOS!")
        sys.exit()
        


    operaciones={1:sumar,2:restar,3:multiplicar,4:dividir,5:exponencial,6:salir}

  

    try:

        if opcion>0 and opcion<6:
            a,b=introduccion()
        
        respuesta=operaciones[opcion]

        respuesta()

        opcion=0

    except (KeyError,NameError):
        print ("Introduce una opción correcta.")
    
    
    
    print ("\n")

   




