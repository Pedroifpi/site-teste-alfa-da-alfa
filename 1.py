# Calcula os n primeiros números da sequência de Fibonacci
n = 10
fibonacci_numbers = []
a, b = 0, 1
for _ in range(n):
    fibonacci_numbers.append(a)
    a, b = b, a + b

# Calcula o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Calcula o fatorial dos números ímpares da sequência de Fibonacci
for number in fibonacci_numbers:
    if number % 2 != 0:
        # Calcula o fatorial usando uma função interna
        fatorial_result = 1
        for i in range(1, number + 1):
            fatorial_result *= i
        print(f"Fatorial de {number}: {fatorial_result}")
