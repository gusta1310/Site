casa = float(input('digite o valor da casa: '))
salario = float(input('digite o salario: '))
anos = int(input('quantas parcelas pra pagar: '))

prestação = casa / (anos * 12)
minimo = (salario * 30/100)

print(f'pra pagar uma casa de {casa} em {anos} anos')
print(f'a prestação será de {prestação}')

if prestação > minimo:
    print('não será possivel a negociação')
elif prestação <= minimo:
    print('podemos negociar')

