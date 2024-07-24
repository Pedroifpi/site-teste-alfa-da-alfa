# Questão 8: Escreva um programa que crie uma lista bidimensional utilizando list comprehension e imprima a diagonal principal.

matriz = [[1 + i + j*5 for i in range(5)] for j in range(5)]
diagonal = [matriz[i][i] for i in range(5)]
print("Matriz:")
for linha in matriz:
    print(linha)
print("Diagonal principal:", diagonal)