from unidecode import unidecode
import string

def normalizar(cadena):
    cadena = unidecode(cadena.lower())
    for c in string.punctuation:
        cadena = cadena.replace(c,'')
    return cadena

def contar_palabras(lista,palabra):
    cont = 0
    for c in lista:
        if c == palabra:
            cont+=1
    return cont
    
def imprimir(lista):
    for i in lista:
        print(i)

cadena = "Hola, qué haces? Cómo estás?"

lista_de_palabras = normalizar(cadena).split(' ')

lista_impresiones = []

for palabra in lista_de_palabras:
    impr = f'{palabra}\taparece\t{contar_palabras(lista_de_palabras,palabra)}\tveces'
    if not(impr in lista_impresiones):
        lista_impresiones.append(impr)

imprimir(lista_impresiones)