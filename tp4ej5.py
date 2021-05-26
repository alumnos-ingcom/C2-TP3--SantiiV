################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    if numero == 0:
        return "El número es 0"
    elif numero > 0:
        return "El número es positivo"
    else:
        return "El número es negativo"
    
def prueba():
    numero = float(input("Ingrese un número "))
    print(signo(numero))
    
if __name__ == "__main__":
    prueba()
    
