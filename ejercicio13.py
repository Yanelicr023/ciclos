'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
ab = 10 
c = 0
for i in range(1,21):
    print(f"El total a pagar en el mes {i} es de: {ab}")
    c = c + ab
    ab *= 2
    
print(f"El total a pagar por los 20 meses es de: {c}")