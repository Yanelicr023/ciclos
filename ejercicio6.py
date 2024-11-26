'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
limite = int(input("Cuantos numeros quieres escribir: "))
cmenor = 0
cigual = 0
cmayor = 0
for i in range(1,limite + 1):
    n = int(input(f"Escribe el numero {i}: "))
    
    if n > 0:
        cmayor += 1
    elif n < 0:
        cmenor += 1
    else:
        cigual += 1
        
print(f"De los numeros introducidos {cmayor} son mayores que 0")
print(f"De los numeros introducidos {cmenor} son menores que 0")
print(f"De los numeros introducidos {cigual} son iguales a 0")