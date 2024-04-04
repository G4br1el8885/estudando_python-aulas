# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com  15% de aumento.
pay = int(input('insira o salário de seu funcionário:'))
pup = pay + int((pay * 0.15))
print('Seu salário recebeu 15% de aumento! Agora você receberá R${}'.format(pup))
