# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle, choices

name1 = input('Isira o nome do aluno 1:')
name2 = input('Insira o nome do aluno 2:')
name3 = input('Insira o nome do aluno 3:')
name4 = input('Insira o nome do aluno 4:')

lista = [name1, name2, name3, name4]
shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))