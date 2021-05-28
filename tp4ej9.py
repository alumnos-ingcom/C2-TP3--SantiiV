################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################
def es_primo(numero):
    contador = 0 
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
            
    if contador == 2:
        return "es primo"
    else:
        return "no es primo"


def prueba():
    numero = int(input("Ingrese un número para saber si es primo "))
    print("El numero ingresado", es_primo(numero))


if __name__ == "__main__":
    prueba()