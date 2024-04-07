# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: 6.127 -- 6
import math
n = float(input('insira um número real qualquer:'))
print('A porção inteira de {} é {}'.format(n, math.trunc(n)))