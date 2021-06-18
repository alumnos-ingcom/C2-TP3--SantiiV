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
    lista = []
    longitud_lista = 3
    print("Ingrese 3 valores")
    while longitud_lista > 0:
        ingreso = int(input("Valor a agregar: "))
        lista.append(ingreso)
        longitud_lista -= 1
        
    valoruno = lista[0]
    valordos = lista[1] 
    valortres = lista[2]
    
    print("Mayor a menor:")
    resultadouno = ordenar_mayor_a_menor(valoruno, valordos, valortres)
    print(resultadouno)
    
    print("Menor a mayor:")
    resultadodos = ordenar_menor_a_mayor(valoruno, valordos, valortres)
    print(resultadodos)


if __name__ == "__main__":
    prueba()