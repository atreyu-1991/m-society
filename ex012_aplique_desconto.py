#Leia um valor de mostre ele com desconto de 5%
valor = float(input('Digite o valor do produto: R$ '))
desconto = valor - (valor * 5 / 100)
print(f'O valor R${valor} com 5% de desconto, ficará R$ {desconto}')