# 05

frase = input('Digite uma frase: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u', 'á' 'é', 'í', 'ó', 'ú', 'ã', 'õ']
contador = 0
indice = []

for i in range(len(frase)):
    if frase[i] in vogais:
        contador += 1
        indice.append(i)
        
print(f'Quantidade de vogais: {contador}')
print(f'Posições: {indice}')
        