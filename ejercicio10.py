'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''
print('Calcular potencia')

base = float(input('Escribe la base: '))
exp = int(input('Escribe la potencia: '))
r = 1
for i in range(1,exp + 1):
    r *= base 
    
print(f'El resultado es: {r}')