# 01
import os
frase = input('Digite uma frase: ')
nome_arquivo = 'frase.txt'
# Caminho completo do arquivo (no mesmo diretório do script)
caminho_arquivo = os.path.abspath(nome_arquivo)
# Escrevendo a frase no arquivo
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(frase)
    
print(f'Frase salva em {caminho_arquivo}')