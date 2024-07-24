km = float(input("Quantidade de Km percorridos: "))
dias = int(input("Quantidade de dias alugados: "))
preco_total = (dias * 60) + (km * 0.15)
print(f"Preço total a pagar: R$ {preco_total:.2f}")