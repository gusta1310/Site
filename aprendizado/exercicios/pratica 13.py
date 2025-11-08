import random

n1 = input("digite o primeiro aluno: ")
n2 = input("digite o segundo aluno: ")
n3 = input("digite o terceiro aluno: ")
n4 = input("digite o quarto aluno: ")

list = [n1,n2,n3,n4]

escolhidos = random.choice(list)

print(f'o aluno escolhido foi {escolhidos}')

#random.choice escolhe um elemento dentro de uma lista