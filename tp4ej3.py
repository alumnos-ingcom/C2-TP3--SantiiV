################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def convertir_a_fahrenheit(centigrados):
    fahrenheit = ((float(centigrados) * 1.8) + 32)
    return fahrenheit

def prueba():
    ingreso = input("Ingrese grados centígrados ")
    print("Resultado en Fahrenheit:", convertir_a_fahrenheit(ingreso))

if __name__ == "__main__":
    prueba()
