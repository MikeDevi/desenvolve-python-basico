# 04

import random

# Função para imprimir o enforcado
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Lê as palavras do arquivo de gabarito
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f if linha.strip()]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)
letras_descobertas = ['_' for _ in palavra_secreta]
letras_digitadas = []

# Lê os estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Divide os estágios do enforcado em uma lista
estagios = conteudo.strip().split('\n\n')

# Variáveis do jogo
tentativas = 6
erros = 0

print("=== JOGO DA FORCA ===")
print(f"A palavra tem {len(palavra_secreta)} letras.")

# Loop principal do jogo
while erros < tentativas and '_' in letras_descobertas:
    print("\nPalavra:", ' '.join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in letras_digitadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        erros += 1
        print(f"Errou! ({erros}/{tentativas} tentativas)")
        imprime_enforcado(erros, estagios)

# Fim do jogo
if '_' not in letras_descobertas:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)
    imprime_enforcado(erros, estagios)
