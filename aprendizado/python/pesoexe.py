peso = int(input("digite seu peso:"))
altura = float(input("digite sua altura?:"))
imc = peso/altura**2

if imc < 20:
    print("abaixo do peso")
    
elif imc < 25:
    print("peso normal")
    
elif imc < 30:
    print("sobrepeso")
    
elif imc < 40:
    print("obeso")
    
else:
    print("outros")