################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def compara(valoruno, valordos):
    if valoruno == valordos:
        return 0
    elif valoruno > valordos:
        return 1
    else:
        return -1
        
def prueba():
    valoruno = int(input("Ingrese el primer valor" + " #"))
    valordos = int(input("Ingrese el segundo" + " #"))
    print(compara(valoruno, valordos))

if __name__ == "__main__":
    prueba()