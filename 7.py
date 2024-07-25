# Entrada de dados: uma lista de 20 inteiros
lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(20)]

# Calculando a moda
frequencias = {}
for numero in lista:
    if numero in frequencias:
        frequencias[numero] += 1
    else:
        frequencias[numero] = 1

moda = max(frequencias, key=frequencias.get)

# Calculando a mediana
lista_ordenada = sorted(lista)
tamanho = len(lista_ordenada)
if tamanho % 2 == 0:
    mediana = (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2
else:
    mediana = lista_ordenada[tamanho // 2]

# Calculando a média
media = sum(lista) / tamanho

# Exibindo os resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Média: {media:.2f}")
