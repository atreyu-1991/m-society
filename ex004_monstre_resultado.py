#Leia algo e mostre as possiveis informações sobre
algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Está em letras maiúsculas? {algo.isupper()}')
print(f'Está em letras minúsculas? {algo.islower()}')
print(f'É numérico? {algo.isnumeric()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É iniciado em maiúscula? {algo.istitle()}')
print(f'É somente espaços? {algo.isspace()}')