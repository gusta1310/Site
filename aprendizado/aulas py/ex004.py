from math import sqrt                              # IMPORT = IMPORTA MODULOS DE SUA PREFERENCIA

num =int(input('digite um numero: '))              # importa operações matematicas automaticamente
raiz = sqrt(num)
raiz = round(raiz, 2)

print(f'a raiz de {num} é igual á {raiz}')


import random

num = random.random()     # RANDOM = gera um numero aleatorio no sistema
print(num)

num1 = random.randint(1, 10)     #random.radiant() = gera de um determinado numero até outro determinado numero
print(num1)

import emoji
print(emoji.emojize("olá mundo 😀" ))