#calcule a quantidade de KM percorrido por um carro e quantidade de dias e dê o valor do aluguel
#custo do carro 60 reais e custo do KM percorrido 0.15 centavos
dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos KM percorridos? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor de dias alugados é de R${dias * 60:.2f} e de Km percorridos é de R${km * 0.15:.2f}.\nO valor total a ser pago é de R${pago:.2f}')