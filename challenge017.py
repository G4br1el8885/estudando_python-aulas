# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
cato = int(input('Qual o valor do cateto oposto?(cm):'))
cata = int(input('Qual o valor do cateto adjacente?(cm):'))
hip = sqrt(cato ** 2 + cata ** 2)
print('A hipotenusa, de acordo com Pitágoras equivale a: {:.2f}cm'.format(hip))