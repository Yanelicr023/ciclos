'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
print("Identificador de vocales (para salir ingresa espacio)")

while True:
    l = input("Escribe una letra: ")
    l = l.upper()
    
    if l == " ":
        break
    else:
        if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U' :
            print("ES VOCAL")
        else:
            print("NO ES VOCAL") 