# Escreva um programa que leia um valor em metros e converta para centímetros e milímetros

m = float(input('Quantos metros deseja transformar?'))
km = m / 1000
cm = m * 100
mm = m * 1000
print('É equivalente a {}km\nÉ equivalente a {}cm\nÉ equivalente a {}mm'.format(km, cm, mm))
