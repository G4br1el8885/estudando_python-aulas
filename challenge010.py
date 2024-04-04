# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar - Considere U$5,06

dol = float(input('Quantos dol. tens?'))
Rs = dol * 5.06
print('Você tem R${:.2f}'.format(Rs))