#Leia um número real qualquer e mostre na tela sua porção inteira
from math import trunc
num = float(input('Digite um número: '))
por = trunc(num)
print(f'O número {num} tem como sua porção inteira de {por}')