################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def convertir_a_centigrados(fahrenheit):
    centigrados = ((float(fahrenheit) - 32)/ 1.8)
    return centigrados
    
def prueba():
    ingreso = input("Ingrese grados fahrenheit ")
    print("Resultado en centígrados:", convertir_a_centigrados(ingreso))

if __name__ == "__main__":
    prueba()
