#Faça um programa que leia os nomes dos alunos e sorteie um deles para apagar a lousa
from random import choice
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno(a) escolhido(a) para apagar a lousa é o(a): {escolhido}')