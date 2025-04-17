# 07

import random

def encrypt(lista_de_nomes):
    n = random.randint(1, 10)  # chave de criptografia
    criptografados = []

    for nome in lista_de_nomes:
        novo_nome = ''
        for c in nome:
            codigo = ord(c)
            if 33 <= codigo <= 126:
                novo_codigo = ((codigo - 33 + n) % 94) + 33
                novo_nome += chr(novo_codigo)
            else:
                novo_nome += c  # mantém se estiver fora do intervalo visível
        criptografados.append(novo_nome)

    return criptografados, n

nomes = ["Alice", "Bob!", "João#123"]
criptografados, chave = encrypt(nomes)

print("Criptografados:", criptografados)
print("Chave:", chave)

        