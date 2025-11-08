distancia = float(input('digite a distancia'))

preço = round(2)
preço1 = round(2)

if distancia <= 200:
    preço = (distancia * 0.50)
    print(f'{preço}')
else:
    preço1 = (distancia * 0.45)
    print(f'{preço1}')