#Leia o comprimento dos catetos, calcule e mostre o valor da hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir: {hi:.2f}')