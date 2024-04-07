# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

name1 = input('Isira o nome do aluno 1:')
name2 = input('Insira o nome do aluno 2:')
name3 = input('Insira o nome do aluno 3:')
name4 = input('Insira o nome do aluno 4:')
lista = [name1, name2, name3, name4]

ord1 = random.choice(lista)
ord2 = random.choice(lista)
ord3 = random.choice(lista)
ord4 = random.choice(lista)


print('A ordem de apresentação será:\n1-{}\n2-{}\n3-{}\n4-{}'.format(ord1, ord2, ord3, ord4))