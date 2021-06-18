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
    lista = []
    
    longitud_lista = int(input("Cuántos valores desea cargar a la lista? "))

    while longitud_lista > 0:
        ingreso = int(input("Valor a agregar: "))
        lista.append(ingreso)
        longitud_lista -= 1

    print("El menor es:", minimo(lista))
    print("El maximo es:", maximo(lista))

    
if __name__ == "__main__":
    prueba()