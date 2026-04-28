print("Hello, World!")

saludo = "Hola, Mundo!"
print(saludo)
def saludar(nombre):
    return f"Hola, {nombre}!"


#Llenar una funcion para sumar hasta 4 numeros
def sumar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
#Ejemplo de uso de la funcion sumar
print(sumar(1, 2))  # Salida: 3
print(sumar(1, 2, 3))  # Salida: 6
print(sumar(1, 2, 3, 4))  # Salida: 10  

Pene = "Pene"
print(Pene)
print(saludar("Mundo"), sumar(1, 2, 3, 4), Pene)

print(saludar("Alice"))  # Salida: Hola, Alice!
print(saludar("Bob"))    # Salida: Hola, Bob!
