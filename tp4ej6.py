################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def minimo(lista):
    menor = lista[0]
    
    for n in lista:
        if n < menor:
            menor = n
    return menor
    

def maximo(lista):
    maximo = lista[0]
    
    for n in lista:
        if n > maximo:
            maximo = n
    return maximo


def prueba():
    print("Ingrese 5 números")
    a = int(input("# "))
    e = int(input("# "))
    i = int(input("# "))
    o = int(input("# "))
    u = int(input("# "))

    lista = [a, e, i, o, u]
    print("El menor es:", minimo(lista))
    print("El maximo es:", maximo(lista))

    
if __name__ == "__main__":
    prueba()