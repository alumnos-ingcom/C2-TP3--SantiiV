################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def division_lenta(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor: 
        dividendo = dividendo - divisor
        cociente += 1
        
    print("El cociente es:", cociente)
    print("El resto es:", dividendo)
             
   
def prueba():
    dividendo = int(input("Ingrese el dividendo "))
    divisor = int(input("Ingrese el divisor "))
    print(division_lenta(dividendo, divisor))


if __name__ == "__main__":
    prueba()
