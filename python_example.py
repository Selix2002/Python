import random

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