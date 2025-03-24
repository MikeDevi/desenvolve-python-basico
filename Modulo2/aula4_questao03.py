# 03
produto01 = input('Digite o nome do produto 1 ')
vlr_prod01 = float(input('Digite o preço unitário do produto 1 '))
qtd_prod01 = int(input('Digite a quantidade do produto 1 '))
produto02 = input('Digite o nome do produto 2 ')
vlr_prod02 = float(input('Digite o preço unitário do produto 2 '))
qtd_prod02 = int(input('Digite a quantidade do produto 2 '))
produto03 = input('Digite o nome do produto 3 ')
vlr_prod03 = float(input('Digite o preço unitário do produto 3 '))
qtd_prod03 = int(input('Digite a quantidade do produto 3 '))

total = (vlr_prod01 * qtd_prod01) + (vlr_prod02 * qtd_prod02) + (vlr_prod03 * qtd_prod03)
print(f'Total R$: {total}')