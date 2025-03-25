import random
import string
#1. Crea una función `calculadora` que reciba dos números y una operación (`+`, `-`, `*`, `/`) y retorne el resultado.
def calculadora(x,y,operacion):
    if operacion == '+':
        return x+y
    elif operacion == '-':
        return x-y
    elif operacion == '*':
        return x*y
    elif operacion == '/':
        return x/y
    else:
        return "No ingreso un operador valido"
#Escribe una función que reciba una cadena de texto y retorne un diccionario con el conteo de cada palabra.

def conteoDiccionario(texto = "Escribe una función que reciba una cadena de texto y retorne un diccionario con el conteo de cada palabra."):
    palabras = texto.split()  
    diccionario = {}
    j=1
    for i in palabras:
        diccionario[i] = j
        j=j+1
    print(diccionario)

#Crea una función que determine si una palabra o frase es un palíndromo (se lee igual al derecho que al revés).
def palindromo(p1):
    if p1[::-1] == p1:
        print("True")
        return True
    else:
        print("False")
        return False
    
#Implementar una función que genere una contraseña aleatoria de una longitud dada, combinando letras, números y símbolos. Permite que el usuario elija si desea incluir mayúsculas, números o caracteres especiales. Long,OnMayus,OnNumber,OnSpecial
import random
import string

def randomPassword(Long, OnMayus, OnNumber, OnSpecial):
    caracteres_especiales = string.punctuation
    password = ""
    i = 0
    opciones = [string.ascii_lowercase]  
    if OnMayus:
        opciones.append(string.ascii_uppercase)
    if OnNumber:
        opciones.append(string.digits)  
    if OnSpecial:
        opciones.append(caracteres_especiales)

    while i < Long:
        grupo = random.choice(opciones)
        password += random.choice(grupo)
        i += 1

    return password
#Crea una función que convierta una temperatura de Celsius a Fahrenheit y viceversa.
def calcTemperatura(unidad, temperatura):
    if unidad == 'c':

        temperatura_total = (temperatura * 9/5) + 32
        return f"{temperatura_total:.2f}°F"
    
    elif unidad == 'f':
        temperatura_total = (temperatura - 32) * 5/9
        return f"{temperatura_total:.2f}°C"
    
    else:
        return "Unidad no válida. Usa 'c' para Celsius o 'f' para Fahrenheit."

#print(calcTemperatura('c', 100))  # De Celsius a Fahrenheit
#print(calcTemperatura('f', 212))  # De Fahrenheit a Celsius

#7. Escribe una función que reciba una cadena y retorne cuántas vocales y consonantes contiene.
def tipo_letra(palabra):
    vocales = 0
    consonantes = 0

    for letra in palabra:
        if letra.lower() in "aeiou":
            vocales += 1
        elif letra.isalpha():
            consonantes += 1
        else:
            return "Debes ingresar una palabra válida"
    
    return f"Cantidad de vocales: {vocales} y cantidad de consonantes: {consonantes}"

print(tipo_letra('Sebas'))



def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            intento = int(input("Introduce tu intento: "))
            intentos += 1

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print(f"NUMERO ADIVINADO. Cantidad de intentos: {intentos}.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
adivina_el_numero()

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia