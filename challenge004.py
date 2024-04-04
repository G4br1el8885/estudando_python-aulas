# O desafio é fazer um programa que leia algo pelo teclado e mostre na tela o seu tipo primitvo e todas as possíveis informações sobre ele
inf = (input('Type something. I"ll categorize it:'))
print('This information is:')
print(type(inf))
print('Is this numeric?', inf.isnumeric())
print('Is this alphabetic?', inf.isalpha())
print('Is this printable?', inf.isprintable())
print('Is this upper (maiúsculo)?', inf.isupper())
