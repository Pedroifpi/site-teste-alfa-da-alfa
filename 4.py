mensagem = input("Digite a mensagem para criptografar: ")
chave = 3
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
criptografada = ''

for letra in mensagem:
    if letra in alfabeto:
        nova_posicao = (alfabeto.index(letra) + chave) % 26
        criptografada += alfabeto[nova_posicao]
    else:
        criptografada += letra

print("Mensagem criptografada:", criptografada)