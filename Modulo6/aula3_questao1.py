# 01
lista = []
print('Digite pelo menos 4 números inteiros ou digite "Fim" para encerrar')

while len(lista) < 6:
    num = int(input('Digite um valor \n'))
    if num == 'Fim':
        break
    else:
        lista.append(num)

print(f'Valor original da lista: {lista}')
print(f'3 Primeiros elementos: {lista[:3]}')
print(f'Os 2 últimos elementos: {lista[-2:]}')
print(f'A lista invertida (do fim para o começo): {lista[::-1]}')
print(f'Os elementos de índice par: {lista[1::2]}')
print(f'Os elementos de índice ímpar: {lista[0::2]}')


