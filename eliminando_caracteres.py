#  Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como
#             salida (out1, out2).
#  - out1 contendrá todos los caracteres presentes en la str1, pero NO estén presentes en str2.
#  - out2 contendrá todos los caracteres presentes en la str2, pero NO estén presentes en str1.

def findNonCommon(str1, str2):
    ora = ''
    for c in str1:
        if str2.find(c) == -1:
            ora += c
    return ora

def printNonCommon(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    print('\nCadena 1: ' + findNonCommon(str1,str2))
    print('\nCadena 2: ' + findNonCommon(str2,str1))


printNonCommon('Anita','JUAN')