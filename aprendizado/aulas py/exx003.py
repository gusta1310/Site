n = input('Digite algo: ')

print(n.isalnum(),n.isupper(),n.isdecimal(),n.istitle(),n.isidentifier(),n.isspace())

h = int(input('Digite um numero: '))
#--------------------------------------------------------------------------------------------------

if h >= 5:
    print('verdadeiro')                     #if else, sistema de repetição
else:
    print('falso')
#----------------------------------------------------------------------------------------------------

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o primeiro numero: '))
                                                    #tipo de calculo
s = n1 + n2
print(f'a soma entre {n1} + {n2} = {s}')
#-----------------------------------------------------------------------------------------------------

f = 5 % 2
print(f'o valor calculado é de: {f}')               #calculo 'resto' da divisão

#------------------------------------------------------------------------------------------------------

#1 ()
#2 **                                           #Ordem de procêdencia para qualquer tipo de cálculo
#3 * / // %
#4 + -

#------------------------------------------------------------------------------------------------------

nome = input("digite o nome ")
print("prazer \n em velo {:20}!".format(nome))         #repetição com {:20}    #\n é quebra de linha

#------------------------------------------------------------------------------------------------------

n1 = int(input('digite um valor: '))
n2 = int(input('digite  outro valor: '))

a = n1 + n2
s = n1 - n2
v = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2

round(d,2)

print(f"os resultados são {a}, {s}, {v}, {d}, {p},{di} ")