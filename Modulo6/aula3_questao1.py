# 01
lista = []
num = 0
while num == 1:
    num = int(input('Digite um valor \nOu digite "1" para sair '))
    lista.append(num)

print(f'Valor original da lista: {lista}')
print(f'3 Primeiros elementos: {lista[:3]}')