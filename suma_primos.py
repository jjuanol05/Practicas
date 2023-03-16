import os
""" Calcula lo que suman los primeros numeros primos que hay entre 1000 y 2000 """

""" Ordena descendentemente un array de números enteros (mayor a menor) 
    El método de ordenamiento es de libre elección """

""" Busca si cierto número entero (leido por teclado) existe en un array """

def ItsPrimo(num: int) -> bool:
    primo = True
    if num != 1:
        for i in range(1,num+1):
            div = num/i
            n,d = div.as_integer_ratio()
            if n != num:
                if n != 1:
                    if d == 1:
                        primo = False           
        return primo
    else:
        return False
    
def SumaPrimos(num1: int, num2: int) -> int:        
    suma = 0
    for i in range(num1, num2 + 1):
        if ItsPrimo(i):
            suma += i
    return suma

if __name__ == '__main__':
    print(f'\nSuma total de numeros primos entre 1000 y 2000: {SumaPrimos(1000,2000)}\n')