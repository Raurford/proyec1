#tabla de multiplicar de un numero ingresado segundo actividad 

numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#segundo ejercicio realizar tabal de multiplicar del 1 al 10 
for numero in range(1, 11):
    print(f"Tabla de multiplicar del {numero}:",end="\t")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
#ejercicio 3 
frase = input("Ingrese una frase: ")

frase = frase.lower()

vocales = 0
vocales_encontradas = []

for c in frase:
    if c in "aeiou":
        vocales += 1
        if c not in vocales_encontradas:
            vocales_encontradas.append(c)

print(f"La frase contiene {vocales} vocales.")
print("Las vocales que aparecen en la frase son:", vocales_encontradas)
#ejecicio 4
costo = float(input("Ingrese el costo del artículo: "))
cantidad = int(input("Ingrese la cantidad comprada: "))

precio_venta = (costo * cantidad) * 1.3

print(f"El precio de venta para obtener una ganancia del 30% es: {precio_venta:.2f}")