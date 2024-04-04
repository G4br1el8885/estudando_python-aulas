# o '.isnumeric' diz se é possível converter aquele valor numérico em 'int' - independente de seu tipo primitivo
# o '.isalpha' diz se é alfabético - independente de seu tipo primitivo
# o '.isalnum' diz se é alfanumérico, ou seja, se tem números com letras, ou números ou letras
# Existem vários tipos de 'is...' para confirmar informações sobre algum objeto

n1 = str(input('Digite algo'))
print(n1.isalnum(), type(n1))


