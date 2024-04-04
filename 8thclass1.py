
# Curso Python 08 - Utilizando Módulos (bibliotecas de códigos expandidos para as mais diversas funções)
# Utiliza-se: 'import vmodule'; ou, para importar(incorporar ao programa) comandos específicos: 'from vmodule import vfunction'
import math
from math import sqrt

# Formula: c * (1+i) ** t
c = float(input('Insira o aporte inicial:'))
i = float(input('insira a taxa de juros a.a')) / 100
t = int(input('insira o tempo (em anos)'))
vall = c * (1+i) ** t
renda = vall - c
rendam = renda / 12
rendad = renda / 30
print('O valor líquido após {} anos, será de {:.2f}'.format(t, vall))
print('A renda será de {:.2f}'.format(renda))
print('A renda mensal será de {:.2f}\nA renda diária será de {:.2f}'.format(rendam, rendad))
# tá errado

