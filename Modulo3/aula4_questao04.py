# 04
distancia = int(input('Digite a distancia do frete em Km '))
peso = int(input('Digite o peso do produto em Kg '))

if distancia <= 100:
    valor_frete = peso * 1
    #print(f'Distância de {distancia} valor do frete R$: {valor_frete}')
elif 101 < distancia < 300:
    valor_frete = peso * 1.50
   # print(f'Distância de {distancia} valor do frete R$: {valor_frete}')
elif distancia > 300:
    valor_frete = peso * 2
   # print(f'Distância de {distancia} valor do frete R$: {valor_frete}')
if peso > 10:
    valor_frete += 10
    print(f'Distância de {distancia} valor do frete R$: {valor_frete}')
else:
    print(f'Distância de {distancia} valor do frete R$: {valor_frete}')
