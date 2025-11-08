n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

if n1 > n2:
    print('o primeiro valor é maior')
elif n2 > n1:
    print('o segundo valor é maior')
elif n1 == n2:
    print('não existe valor maior os dois são iguais')