peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif imc <= 24.9:
    condicao = "Peso ideal (parabéns)"
elif imc <= 29.9:
    condicao = "Levemente acima do peso"
elif imc <= 34.9:
    condicao = "Obesidade grau I"
elif imc <= 39.9:
    condicao = "Obesidade grau II (severa)"
else:
    condicao = "Obesidade grau III (mórbida)"

print(f"IMC: {imc:.2f} - {condicao}")