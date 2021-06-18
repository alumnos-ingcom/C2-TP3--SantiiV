################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def factores_primos(numero):
    primos = []
    for i in range(2, numero+1):
        while numero % i == 0:
            primos.append(i)
            numero = numero / i
    return primos


def prueba():
    numero = int(input("Ingrese un número entero positivo "))
    print("Los factores primos del número ingresado son:")
    print(factores_primos(numero))


if __name__ == "__main__":
    prueba()