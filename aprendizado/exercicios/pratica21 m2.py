ano = int(input('digite seu ano de nascimento: '))

atual = 2025
idade = atual - ano


if idade == 18:
    print('é hora de se alistar paeeeee!!!!!')

elif idade < 18:
    saldo = 18 - idade
    print(f'vc ainda vai se alistar garotinnnn calmaaaa, faltam {saldo} anos!!! ')
    # saldo = 18 - idade calculo pra saber quantos falta
elif idade > 18:
    saldo = idade - 18
    # saldo = idade - 18 calculo pra saber quntos sobram
    print(f'tá querendo ser preso rapaz, VAI JÁ SE ALISTAR VAGABUNDO, JÁ PASSOU {saldo} anos !!! 😡')