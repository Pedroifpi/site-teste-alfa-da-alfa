def fibonacci(n):
  """Calcula os n primeiros números da sequência de Fibonacci."""
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

def fatorial(n):
  """Calcula o fatorial de um número."""
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)

# Calcula os 10 primeiros números da sequência de Fibonacci
fibonacci_numbers = list(fibonacci(10))

# Calcula o fatorial dos números ímpares da sequência de Fibonacci
for number in fibonacci_numbers:
  if number % 2 != 0:
    print(f"Fatorial de {number}: {fatorial(number)}")