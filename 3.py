# Questão 3: Escreva um programa que calcule o imposto de renda a partir do salário de um funcionário com base na tabela fornecida e repita até que o usuário deseje encerrar.

while True:
    salario = float(input("Digite o salário (ou -1 para sair): "))
    if salario == -1:
        break
    if salario <= 1903.98:
        imposto = 0
    elif salario <= 2826.65:
        imposto = salario * 0.075 - 142.80
    elif salario <= 3751.05:
        imposto = salario * 0.15 - 354.80
    elif salario <= 4664.68:
        imposto = salario * 0.225 - 636.13
    else:
        imposto = salario * 0.275 - 869.36
    print(f"Imposto a pagar: R${imposto:.2f}")