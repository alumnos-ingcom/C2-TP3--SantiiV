################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def suma_lenta(numero, otro_numero):
    resultado = numero + otro_numero

    print("El resultado es:")
    while numero < resultado:
        numero += 1
        print(numero)
        
    while numero > resultado:
        numero -= 1
        print(numero)
        
    if numero == 0:
        print("0")

def prueba():
    numero = int(input("Ingrese el primer número a sumar "))
    otro_numero = int(input("Ingrese el segundo "))
    suma_lenta(numero, otro_numero)

if __name__ == "__main__":
    prueba()