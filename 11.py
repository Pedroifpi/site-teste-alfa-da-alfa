notas = [float(input(f"Digite a nota do exame {i+1}: ")) for i in range(5)]

media = sum(notas) / len(notas)

if all(nota >= 7 for nota in notas):
    classificacao = "A - passou em todos os exames"
elif all(nota >= 7 for nota in notas[:4]) and notas[4] < 7:
    classificacao = "B - passou em I, II e IV, mas não em III ou V"
elif all(nota >= 7 for nota in notas[:3] + notas[3:4]) and notas[4] < 7:
    classificacao = "C - passou em I e II, III ou IV, mas não em V"
else:
    classificacao = "Reprovado - outras situações"

print(classificacao)