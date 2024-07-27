# Número de elementos da sequência de Fibonacci a serem considerados
n_elementos = 10

# Lista para armazenar os primeiros números de Fibonacci
fibonacci = [0, 1]

# Gerar os primeiros n números de Fibonacci
while len(fibonacci) < n_elementos:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Calcular e imprimir o fatorial dos números ímpares da sequência
for numero in fibonacci:
    if numero % 2 != 0:
        # Calcular o fatorial do número
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        print(f"Fatorial de {numero} é {fatorial}")
