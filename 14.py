# Solicita ao usuário o número até onde procurar os números primos
n = int(input("Digite um número inteiro: "))

# Lista para armazenar os números primos
primos = []

# Verifica se cada número até n é primo
for num in range(2, n + 1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

# Imprime a lista de números primos
print(f"Números primos até {n}: {primos}")