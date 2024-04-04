# Trabalhando com operações aritméticas e variáveis

n1 = int(input('Um número'))
n2 = int(input('Outro número:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
resd = n1 % n2

print('a soma é {}, \n a subtração é {}, \n a multiplicação é {}, \n a divisão é {:.3f}'.format(s, sub, m, d), end=', ')
print('a divisão inteira é {}, e o resto da divisão inteira é {}'.format(di, resd))

# Posso usar "end=''" dentro de 'print' para que o código debaixo continue na mesma line
# Posso usar '\n' dentro de 'print' para que ocorra uma quebra de linha
