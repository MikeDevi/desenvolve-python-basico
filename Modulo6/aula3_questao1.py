# 01
lista = []
n = 0
while n <=5:
    num = int(input('Digite um valor \n'))
    lista.append(num)
    n += 1
    

print(f'Valor original da lista: {lista}')
print(f'3 Primeiros elementos: {lista[:3]}')
print(f'3 Primeiros elementos: {lista[:-1]}')
