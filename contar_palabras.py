from unidecode import unidecode
import string

def normalizar_texto(texto):
    """Esta función normaliza a minúsculas y quita los signos de puntuación a una cadena de texto

    Args:
        texto (str): Cadena de texto a normalizar

    Returns:
        str: Cadena de texto normalizada
    """
    texto_minusculas = texto.lower()
    texto_sin_puntuacion = unidecode(texto_minusculas)
    for caracter in string.punctuation:
        texto_sin_puntuacion = texto_sin_puntuacion.replace(caracter,'')
    return texto_sin_puntuacion

def separar_palabras(cadena_normalizada):
    """Esta función regresa una lista de palabras de una cadena de texto

    Args:
        cadena_normalizada (str): Cadena de texto para separar en palabras

    Returns:
        list[str]: Lista de palabras
    """
    return cadena_normalizada.split(' ')

def contar_palabras(lista_de_palabras):
    """Esta función regresa un diccionario con las veces que una palabra aparece en una lista

    Args:
        lista_de_palabras (list[str]): Lista de palabras para analizar

    Returns:
        dict: Dicccionario que contiene las palabras y el número de veces que aparece en la lista
    """
    diccionario = {}
    for palabra in lista_de_palabras:
        if palabra in diccionario:
            diccionario[palabra] +=1
        else:
            diccionario[palabra] = 1
    return diccionario 

texto = "Hola, qué haces? Cómo estás?"

texto_normalizado = normalizar_texto(texto)

lista_palabras = separar_palabras(texto_normalizado)

palabras_contadas = contar_palabras(lista_palabras)

for palabra in palabras_contadas:
    print(f'La palabra:\t{palabra}\taparece:\t{palabras_contadas[palabra]}\tveces')