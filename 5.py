populacao_a = 5000000
populacao_b = 7000000
taxa_natalidade_a = 0.03
taxa_natalidade_b = 0.02
anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_natalidade_a
    populacao_b += populacao_b * taxa_natalidade_b
    anos += 1

print(f"O país A ultrapassará o país B em {anos} anos.")