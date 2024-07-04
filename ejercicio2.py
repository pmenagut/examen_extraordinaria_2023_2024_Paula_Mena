# Ejercicio 1
def obtener_factores_primos(n):
    factores_primos = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factores_primos.append(divisor)
            n //= divisor
        divisor += 1
    
    return factores_primos

def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero mayor que 1: "))
            if numero > 1:
                return numero
            else:
                print("El número debe ser mayor que 1. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def main():
    numero = solicitar_numero()
    factores = obtener_factores_primos(numero)
    print(f"Factores primos de {numero}: {factores}")

if __name__ == "__main__":
    main()
