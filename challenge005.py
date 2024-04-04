# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('insira um número e direi seu antecessor e sucessor:'))
print('o antecessor de [{:-^3}] é: [{:-^3}] \nO sucessor de [{:-^3}] é: [{:-^3}]'.format(num, num - 1, num, num + 1))