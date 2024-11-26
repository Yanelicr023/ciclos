'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''

import random
aleatorio = random.randint(1,100)

print("Adivina el numero del 1 al 100 ")
x = 10
while True: 
    print(f"Tienes {x} intentos")
    n = int(input("Escribe el numero: "))
    
    if n == aleatorio:
        print("LEEEEE ATINASSSSTEEEE!!!!")
        break
    else:
        x -= 1
        if x == 0:
            print(f"No le atinaste, el numero era: {aleatorio}")
            break
            