# Crie um prigrama que leia uma temperatura em Graus Celsius, e o converta para Graus Farenheit.

c = float(input('Insira a temperatura em Celsius:'))
f = (c * 9 / 5) + 32
print('A temperatura em Farenheit será de {:.1f}F'.format(f))
