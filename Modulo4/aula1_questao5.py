# 05
qtd = int(input('Qual a quantidade de representantes? '))
total_idade = 1

for n in range(qtd):
    idade = int(input(f'Qual a sua idade participante: {n}? '))
    total_idade = total_idade + idade
    n =+ 1
    
media = total_idade / qtd
print('A média de idade é:', media)


