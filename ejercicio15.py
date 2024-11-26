'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
numero = int(input("Ingresa un número entero: "))


binario = ""


if numero == 0:
    binario = "0"


else:
    while numero > 0:
        binario = str(numero % 2) + binario  
        numero = numero // 2 


print(f"El número en binario es: {binario}")