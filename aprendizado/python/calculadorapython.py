num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
operador = input("digite o operador: ")

if operador == '+':
    resultado = num1 + num2
    print(resultado)

elif operador == '-':
    resultado = num1 - num2
    print(resultado)

elif operador == '*':
    resultado = num1 * num2
    print(resultado)

elif operador == '/':
    resultado = num1 / num2
    print(resultado)

else:
    print("operador incorreto")
    
