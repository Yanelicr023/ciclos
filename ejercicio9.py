'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
limite_in = int(input("Escribe el limite inferior: "))
limite_su = int(input("Escribe el limite superior: "))
suma = 0
contf = 0
conti = 0
while True:
    if limite_in >= limite_su:
        limite_in=int(input('El limite inferior no puede ser mayor o igual al superior, REESCRIBELO: '))
    else:
        break