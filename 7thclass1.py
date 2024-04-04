# Ordem de precedência:
# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243

print(5 * 3 ** 2 / 5)  # = 9.0
print(pow(3, 3))  # Outra forma de potenciação


# Posso usar o '+' em strings para concatená-las
print('olá' + 'oi')

# Posso usar '*' em strings para repetí-las
print(8 * 'pau')

# Posso usar o '.format' para formatar os caracteres da forma que eu desejar - Posso dizer quantos espaços eles podem ocupar e preencher esses espaços com um caracter. Ex:{:=^20}
name = input('digite o nome da sua mãe')
print('Olá, {:=^20}! Gostaria de sair para jantar hoje?'.format(name))


