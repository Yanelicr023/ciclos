'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''
n = int(input("Escribe un numero: "))
cs = 0

for i in range(1,n+1):
    r = n % i
    
    if r == 0:
        cs += 1
        
if cs == 2:
    print(f"El numero es Primo ")
else:
    print("El numero no es primo")
    