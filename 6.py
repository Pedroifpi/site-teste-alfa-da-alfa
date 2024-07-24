# Questão 6: Escreva um programa que leia o índice pluviométrico de cada dia do mês de junho e informe o dia que mais choveu, o dia que menos choveu e as médias pluviométricas de cada quinzena.

pluvio = [float(input(f"Índice pluviométrico do dia {i+1}: ")) for i in range(30)]
print(f"Dia com mais chuva: {pluvio.index(max(pluvio))+1}")
print(f"Dia com menos chuva: {pluvio.index(min(pluvio))+1}")
print(f"Média das quinzenas: {sum(pluvio[:15])/15:.2f}, {sum(pluvio[15:])/15:.2f}")