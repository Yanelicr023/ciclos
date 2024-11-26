'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
limite_in = int(input("Escribe el limite inferior: "))
limite_su = int(input("Escribe el limite superior: "))

for i in range(limite_in,limite_su + 1):
    if i % 2 == 0:
        print(i)