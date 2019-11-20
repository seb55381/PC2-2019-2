import random
N = 0
matriz = []
a = []
while True:
    N = int(input("Ingrese el tamaño de la matriz, debe ser entre 2 y 5: "))
    if N >= 2 and N <= 5:
        break
    else:
        print("Ingrese un numero valido")
for i in range (0,N):
    a = []
    for i in range (0,N):
        a.append(random.randrange(1,101)) 
    matriz.append(a)       

for i in matriz:
    print(i)

print("Cantidad de elementos pares:")
p=0
for i in matriz:
    for a in range (0,N):
        if i[a]%2 == 0:
            p+=1

print(p)

