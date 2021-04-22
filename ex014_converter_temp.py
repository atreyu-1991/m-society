#Crie um programa que leia temperatura em C e converta em F
grau = float(input('Digite a temperatura em graus Celsius: '))
fahre = ((grau * 9) / 5) + 32
print(f'A temperatura de {grau}ºC é igual a {fahre}ºF.')