# Questão 3: Escreva um programa que calcule o imposto de renda a partir do salário de um funcionário com base na tabela fornecida e repita até que o usuário deseje encerrar.
while True:
    salario = float(input("Digite o salário do funcionário (ou 0 para sair): "))

    if salario == 0:
        break

    # Calculando o imposto de renda baseado no salário
    if salario <= 1500:
        aliquota = 0.05
    elif salario <= 3000:
        aliquota = 0.08
    elif salario <= 10000:
        aliquota = 0.15
    else:
        aliquota= 0.27

    imposto = salario * aliquota
    salario_com_desconto = salario - imposto

    print(f"Salário bruto: R$ {salario:.2f}")
    print(f"Imposto devido: R$ {imposto:.2f}")
    print(f"Salário com desconto: R$ {salario_com_desconto:.2f}")

    continuar = input("Deseja calcular o imposto para outro salário? (s/n): ")
    if continuar.lower() != 's':
        break
