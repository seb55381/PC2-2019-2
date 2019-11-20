a = []
texto = input("Ingrese texto: ")
letra = input("Ingrese caracter a contar: ")
def contarletra (texto, letra):
    for i in texto:
        a.append(i)
    algo = a.count(letra)
    return algo

a = contarletra (texto, letra)
print(a)