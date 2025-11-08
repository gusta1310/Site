Num1 = int(input('digite o primeiro numero: '))          # Sem o "Int()" os numeros não são somados são juntados apenas
Num2 = float(input('digite o segundo numero: '))         # "float" serve pra numeros com virgula

print(type(Num1))
print(type(Num2))

soma = (Num1 + Num2)

print("a soma entre {} e {} é igual a {}".format(Num1, Num2, soma))
#print('o resultado final entre',Num1 ,'e', Num2, 'é igual', soma)