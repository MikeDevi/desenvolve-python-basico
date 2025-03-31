# 01
import random
n = 0
lista = []
while n <= 20:
    lista_ale = random.randint(-100, 100)
    n += 1
    lista.append(lista_ale)

listaOrdenada = sorted(lista)
listaMenor = min(lista)
listaMaior = max(lista)
print(f'A lista ordenada: {listaOrdenada}')
print(f'A lista original: {lista}')
print(f'A menor valor da lista: {listaMenor}')
print(f'A maior valor da lista: {listaMaior}')