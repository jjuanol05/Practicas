# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

def palindromo(cadena):
    
    cadena = cadena.lower().replace(' ','')     #Quitamos los espacios
    cadena_inv = cadena[::-1]
    return cadena == cadena_inv

print(palindromo('Anita lava la tina'))
print(palindromo('Hola mundo xD'))