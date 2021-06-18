################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

class IngresoIncorrecto(Exception):
    pass

def division_lenta(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor: 
        dividendo = dividendo - divisor
        cociente += 1  
    return cociente, dividendo
             
   
def prueba():
    dividendo = int(input("Ingrese el dividendo "))
    divisor = int(input("Ingrese el divisor "))
    if divisor == 0:
        raise IngresoIncorrecto("Error. El divisor no debe ser 0.")
        
    print("El cociente y resto son:")
    valores = division_lenta(dividendo, divisor)
    print(valores)


if __name__ == "__main__":
    prueba()
