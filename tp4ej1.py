################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 


def ingreso_entero(mensaje):
    ingreso = input(mensaje + "# ")
    try:
        entero = int(ingreso)
        entero = "entero"
    except ValueError as err:
        raise IngresoIncorrecto("No es entero!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos > 0:
        try:
            valor = ingreso_entero(mensaje)
            return valor
        except IngresoIncorrecto as error:
            print("No es entero!")
            cantidad_reintentos -= 1
            print(f"Te quedan {cantidad_reintentos} intentos")
    raise IngresoIncorrecto("Te quedaste sin intentos")


def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    ingreso = input(mensaje + "# ")
    try:
        valor = int(ingreso)
        if valor >= valor_minimo and valor <= valor_maximo:
            return "correcto"
        else:
            return "incorrecto"
    except ValueError as err:
        raise IngresoIncorrecto("No es entero!") from err
                   

def prueba():
    print("Si desea ultilizar la funcion ingreso_entero presione 1")
    print("Si desea ultilizar la funcion ingreso_entero_reintento presione 2")
    print("Si desea ultilizar la funcion ingreso_entero_restringido presione 3")
    eleccion = input("# ")
    if eleccion == "1":
        numero = ingreso_entero("Ingrese un número entero ")
        print(f"El número ingresado es {numero}")
    elif eleccion == "2":
        numero = ingreso_entero_reintento("Ingrese un número entero ")
        print(f"El número ingresado es {numero}")
    elif eleccion == "3":
        numero = ingreso_entero_restringido("Ingrese un número entero entre 0 y 10 ")
        print(f"El número ingresado es {numero}")
        

if __name__ == "__main__":
    prueba()