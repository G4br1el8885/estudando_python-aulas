# Toda cadeia de texto esta entre aspas (simples ou duplas).
# Toda frase no Python é dividida em números, estes correspondem a seus caracteres. Assim, é possível 'fatiar' strings (frases).
# 'vfrase[5]' caracter digitado (de numero 5)
# 'vfrase[5:11] caracteres desde o 5 até o 10
# 'vfrase[5:11:2] caracteres desde 5 até o 11, mas andando de dois em dois caracteres, ou seja, pulando um.
# 'vfrase[5:] caracteres do 5 até o último. - vale para trás também.
# 'vfrase[5::3] caracteres do 5 até o final, mas indo de três em três caracteres, ou seja, pulando 2.

frase = 'Hello, world. How are you?'

print(frase[:13])