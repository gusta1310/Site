import random

list = [1,2,3,4,5]

n = random.choice(list)

usuario = int(input('digite um numero: '))

if usuario == n:
    print('acertou')
else:
    print('você fracassou')
print(f'o numero escolhido foi {n}')