# Solicita ao usuário que insira um número inteiro
limite = int(input("Digite um número inteiro para encontrar todos os primos até ele: "))

# Lista para armazenar os números primos
primos = []

# Itera sobre todos os números de 2 até o limite
for num in range(2, limite + 1):
    # Assume inicialmente que o número é primo
    eh_primo = True
    
    # Verifica se num tem algum divisor além de 1 e ele mesmo
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    
    # Se o número é primo, adiciona à lista de primos
    if eh_primo:
        primos.append(num)

# Exibe os números primos encontrados
print("Números primos até", limite, "são:", primos)
