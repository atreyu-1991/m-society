#Crie um programa que leia o valor que possui na carteira e quantos dólares e euros pode se comprar com o valor
real = float(input('Quanto dinheiro você tem na carteira? R$: '))
dolar = real / 5.55
euro = real / 6.68
print(f'O valor de R${real} é possível comprar US${dolar:.2f} ou €{euro:.2f}')