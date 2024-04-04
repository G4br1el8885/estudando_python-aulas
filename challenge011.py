# Faça um programa que leia a altura e largura de uma parede em metros, calacule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

alt = float(input('insira a altura de sua parede(m):'))
larg = float(input('insira a largura de sua parede(m):'))
area = alt * larg
paint = area / 2
print('A área do muro é de {:.1f}m2\nA quantidade de tinta será de {:.1f}L'.format(area, paint))