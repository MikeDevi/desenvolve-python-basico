# 03
import random

lista01 = [random.randint(0, 50) for _ in range(random.randint(1, 20))]
lista02 = [random.randint(0, 50) for _ in range(random.randint(1, 20))]
intersecao = []

for i in (lista01):
    if i in lista02:
        intersecao.append(i)
for i in (lista02):
    if i in lista01 and i not in intersecao:
        intersecao.append(i)
        
print(lista01)
print(lista02)
print(f'Esses são os valores presentes nas 2 listas: {intersecao}')