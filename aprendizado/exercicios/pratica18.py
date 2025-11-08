carro = int(input('velocidade do carro: '))

if carro > 80:
    print(f'voce foi multado, a multa vai custar {(carro-80)*7} R$')
else:
    print('está liberado')
