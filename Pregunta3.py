i = []
a = 0

while a != 5:
    persona = input("Ingrese nombre de la persona a inscribirse al curso: ")
    while True:
        sexo = input("Ingrese sexo de la persona a inscribirse al curso (Hombre(h)/Mujer(m)): ")
        if sexo == "h" or sexo == "m":
            break
        else:
            print("Ingrese una respuesta valida")
    while True:
        edad = int(input("Ingrese edad de la persona a inscribirse: "))
        if edad >= 5 and edad <=17:
            a += 1
            d = persona, sexo, edad
            i.append(d)
            break
        else:
            print("Persona no esta en el rango de edades")

print("Lista de inscritos:")
for e in i:
    print("Nombre: " + i[i.index(e)][0])
    print("Sexo: " + i[i.index(e)][1])
    print("Edad: " + str(i[i.index(e)][2]))

print("")
print("Cantidad de hombres y mujeres:")
print("Cantidad de hombres:")
h = 0
for e in i:
    if i[i.index(e)][1] == "h":
        h += 1
print(str(h))
print("Cantidad de mujeres:")
m = 0
for e in i:
    if i[i.index(e)][1] == "m":
        m += 1
print(str(m) + "\n")
print("Promedio de edades:")
promedio_edades = 0
for e in i:
    promedio_edades += i[i.index(e)][2]
promedio_edades = promedio_edades/5
print(str(promedio_edades))
        