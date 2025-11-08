kminicial = float(input("Digite a quilometragem inicial: "))
kmfinal = float(input("Digite a quilometragem final: "))
qtdlitros = float(input("Digite a quantidade de litros gastos: "))
preçolitro = float(input("Digite o preço do litro: "))

d = kmfinal - kminicial

mediaconsumo = d / qtdlitros
valorgasto = qtdlitros * preçolitro

print(f"A distancia percorrida foi: {d}")
print(f"O consumo foi de: %.2f{mediaconsumo}")
print(f"o valor gasto foi: {valorgasto}")