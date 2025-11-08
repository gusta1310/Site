m1 = float(input("digite a primeira nota: "))
m2 = float(input("digite a segunda nota :"))

m = (m1+m2)/2
round(m,2)

print(f'a média final do aluno é {m}')

if m >= 6:
    print('aprovado')
else:
    print('reprovado')


#calculando média dos alunos