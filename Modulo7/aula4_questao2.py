# 02

import re 

arquivo_ex01 = 'frase.txt'
arquivo_ex02 = 'palavras.txt'

with open(arquivo_ex01, 'r', encoding='utf-8') as conteudo:
    ex01 = conteudo.read()
# Extraindo somente palavras do arquivo
palavras = re.findall(r'\b[a-zA-Zá-úÁ-ÚçÇ]+\b', ex01)

#      Nome/Caminho do arquivo / Mod leitura  / códificação
with open(arquivo_ex02, 'w', encoding='utf-8') as f:
    for palavra in palavras:
        f.write(palavra + '\n')   
        
# Lendo o arquivo palavras.txt
with open(arquivo_ex02, 'r', encoding='utf-8') as f:
    print('Conteudo das palavras.txt: \n')
    print(f.read())