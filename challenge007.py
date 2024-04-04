# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

mat = float(input('insira sua nota em Matemática:' ))
port = float(input('insira sua nota em Português:'))
# numberofsubjects = line
fnlmed = (port + mat) / 2
print('sua média final é: {}'.format(fnlmed))
