#Faça um programa que leia o salário de um funcionário e calcule um aumento de 15% no salário
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = salario + (salario * 15 / 100)
print(f'O salário do funcionário era de R${salario} e agora com 15% de aumento será de R${aumento}')