# 03

# Lendo o arquivo (linhas)
with open('estomago.txt', 'r', encoding='utf-8') as estomago:
    linhas = estomago.readlines()

# 01 Primeiras 25 linas   
print('--- Primeiras 25 linas --- \n')
for linha in linhas[:25]:
    # Removendo espaços em branco no início e no final da linha, e quebrando as linhas
    print(linha.strip())

# 02 Número de linhas
numero_linhas = len(linhas)
print('--- Total de linhas --- \n')
print(f'{numero_linhas} Linhas \n')

# 03 Linha com o maior número de palavras (sem  caracteres)
maior_linha = max(linhas, key=len)
print('--- Linha com o maior número de palavras --- \n')
print(f'{len(maior_linha.strip())} caracteres')

# 04 Contagem "Nonato" e "Íria"
numero_palavras = len(maior_linha.split())
texto_final = ' '.join(linhas)

num_nonato = texto_final.count('Nonato')
num_iria = texto_final.count('Íria')    

print(f'--- Número de menções --- \n')
print(f"Nonato: {num_nonato}")
print(f"Íria: {num_iria}")