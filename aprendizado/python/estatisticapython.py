idade = int(input("digite sua idade: "))

if idade < 16:
    print("não eleitor")
    
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatório")
    
elif idade >= 16 and 18 or idade >= 65:
    print("eleitor facultativo")