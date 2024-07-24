saldo_medio = float(input("Digite o saldo médio: R$ "))

if saldo_medio <= 200:
    credito = 0
elif saldo_medio <= 400:
    credito = saldo_medio * 0.20
elif saldo_medio <= 600:
    credito = saldo_medio * 0.30
else:
    credito = saldo_medio * 0.40

print(f"Saldo médio: R$ {saldo_medio:.2f}")
print(f"Valor do crédito: R$ {credito:.2f}")