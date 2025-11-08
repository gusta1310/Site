for c in range(6,0, -2):                        #laço de repetição simples
    print(c)
print('fim')


n = int(input('digite um numero: '))

for c in range(0,n+1):
    print(c)


i = int(input('inicio'))
f = int(input('fim'))
p = int(input('passo'))

for c in range(i, f+1, p):
    print(c)
print('fim')


s = 0

for c in range(0, 4):
    n = int(input("digite um valor: "))
    s = s + n
print(s)
