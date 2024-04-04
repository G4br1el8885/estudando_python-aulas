# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, cocm 5% de desconto.
price = float(input('Preço do produto:'))

print('O produto com 5% de desconto sairá por R${:.2f}'.format(price - price * 0.05))