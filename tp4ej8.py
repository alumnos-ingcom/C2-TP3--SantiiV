################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################
def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos and uno > tres:
        mayor = uno
        if dos > tres:
            medio = dos
            menor = tres
        else:
            medio = tres
            menor = dos
            
    elif dos > uno and dos > tres:
        mayor = dos
        if uno > tres:
            medio = uno
            menor = tres
        else:
            medio = tres
            menor = uno
    else:
        mayor = tres
        if dos > uno:
            medio = dos
            menor = uno
        else:
            medio = uno
            menor = dos
    
    tupla = mayor, medio, menor
    return tupla
   
def ordenar_menor_a_mayor(uno, dos, tres):
    if uno > dos and uno > tres:
        mayor = uno
        if dos > tres:
            medio = dos
            menor = tres
        else:
            medio = tres
            menor = dos
            
    elif dos > uno and dos > tres:
        mayor = dos
        if uno > tres:
            medio = uno
            menor = tres
        else:
            medio = tres
            menor = uno
    else:
        mayor = tres
        if dos > uno:
            medio = dos
            menor = uno
        else:
            medio = uno
            menor = dos
    
    tupla = menor, medio, mayor
    return tupla


def prueba():
    print("Ingrese 3 números")
    a = int(input("# "))
    e = int(input("# "))
    i = int(input("# "))

    print("Mayor a menor:", ordenar_mayor_a_menor(a, e, i))
    print("Menor a mayor:", ordenar_menor_a_mayor(a, e, i))


if __name__ == "__main__":
    prueba()