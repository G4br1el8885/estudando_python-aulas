# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa qeu ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# 'Random' usado para gerar, sortear numeros, elementos,etc.
# Para que o 'random choice' funcione, é necessário que se crie uma "lista" para que ele possa ler e sortear um elemento dessa lista.
import random
name1 = str(input('Insira o nome do aluno 1:'))
name2 = str(input('Insira o nome do aluno 2:'))
name3 = str(input('Insira o nome do aluno 3:'))
name4 = str(input('Insira o nome do aluno 4:'))
lista = [name1, name2, name3, name4]

print('O aluno que apagará o quadro será', random.choice(lista))