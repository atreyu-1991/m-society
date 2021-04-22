#Crie um programa que leia as medidas da parede e mostre quantos litros de tinta será preciso para pintá-la
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'A sua parede tem dimensão de {larg}x{alt} e sua área é de {area}m².')
print(f'Você precisa de {tinta}L de tinta para pintar essa parede.')