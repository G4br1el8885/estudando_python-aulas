# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Radiano é uma outra medida para ângulos. Um radiano equivale a aprox. 57 graus.
# 'radians' serve para converter graus em número radiano, quando se refere à medida de ângulos. É necessário aqui, pois o calculador de seno só entende núemros radianos.
# Como sei a razão entre radianos e graus, posso fazer um conversor de graus para radianos dividindo v.angulo por 57. Existe, contudo a função de 'math' que faz isso: math.radians(num. em graus).
import math
angulo = float(input('Insira a medida do ângulo:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.3f}\nCoseno de {:.3f}\nE tangente de {:.3f}.'.format(angulo, sen, cos, tg))