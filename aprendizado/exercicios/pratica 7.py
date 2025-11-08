p = float(input('digite o preço do produto:R$'))

novo = p - (p*5/100)
novo = round(novo, 2)

print(f'o novo preço do produto já com o desconto de 5% é de: \n {novo} R$')

# pra calcular o desconto de alguma coisa primeiro deve fazer a porcentagem e
# depois subtrair pelo preço original


# ((preço original) * (valor do desconto)/100))

# (preço original) - ((preço original) * (valor do desconto)/100)) 'formula'


