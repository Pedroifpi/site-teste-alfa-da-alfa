cpf = input("Digite o CPF (apenas números): ")

# Remover possíveis caracteres não numéricos
cpf = ''.join([char for char in cpf if char.isdigit()])

# Verificar se o CPF tem 11 dígitos
if len(cpf) != 11:
    print("CPF inválido")
else:
    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    if soma % 11 < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - (soma % 11)
    
    # Calcular o segundo dígito verificador
    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    
    if soma2 % 11 < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - (soma2 % 11)
    
    # Verificar se os dígitos calculados conferem com os fornecidos
    if cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito):
        print("CPF válido")
    else:
        print("CPF inválido")