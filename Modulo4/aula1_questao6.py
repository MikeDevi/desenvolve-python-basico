# 06
qtd_exp = int(input('Digite a quantidade de experimentos '))

n = 0
ratos = 0
coelhos = 0
sapos = 0

for n  in range(qtd_exp):
    tip_cobaia = input(f'Informe o tipo de cobaia : \n Sapo = S, Rato = R, C = Coelho ')
    qtd_cobaia = int(input(f'Digite a quantidade de cobaias '))
    n =+ 1
    if tip_cobaia == 'S':
        sapos =+ qtd_cobaia
    elif tip_cobaia == 'R':
        ratos =+ qtd_cobaia
    elif tip_cobaia == 'C':     
        coelhos =+ qtd_cobaia
    else:
        print('Valor inválido, tente novamente !!')
        
total_cobaias =  ratos + coelhos + sapos
print('Total de cobaias: ', total_cobaias)
print('Total de Coelhos: ', coelhos)
print('Total de Ratos: ', ratos)
print('Total de Sapos: ', sapos)

print(f'Percentual de Coelhos: {coelhos / total_cobaias :.2%}' )
print(f'Percentual de Ratos: {ratos / total_cobaias :.2%}')
print(f'Percentual de Sapos: {sapos / total_cobaias :.2%}')
    
    
    
