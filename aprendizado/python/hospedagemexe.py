tipo = input("digite o tipo da hospedagem:")
quantidade = int(input("digite quantas deseja:"))

if tipo.lower()[0] == "s":
    print("valor a pagar %.2f" %(quantidade * 255.5))
    
elif tipo.lower()[0] == "d":
    
    print("valor a pagar %.2f" %(quantidade * 305.5))
    
else:
    print("tipo de hospedagem invalido")