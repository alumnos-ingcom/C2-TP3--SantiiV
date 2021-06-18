################
# Santiago Vergara - @SantiiV
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_palindromo(texto):
    longitud = len(texto)
    
    if longitud % 2 == 0:
        "Si el texto es par"
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2:]  
    else:
        "Si el texto es impar"
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2 + 1:]
    
    derecha = derecha[::-1]
    
    if izquierda == derecha:
        return True
    else:
        return False
        

def prueba():
    texto = input("Ingrese una frase o palabra para saber si se trata de un palíndromo ")
    texto = es_palindromo(texto)
    print(texto)


if __name__ == "__main__":
    prueba()
