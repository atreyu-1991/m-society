#Leia um ângulo qualquer e mostre na tela seu Seno, Cosseno e Tangente desse ângulo
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tng = tan(radians(angulo))
print(f'O ângulo {angulo} tem como SENO {seno:.2f}, seu COSSENO {coss:.2f} e TANGENTE de {tng:.2f}')