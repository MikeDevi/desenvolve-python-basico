# 03
while True:
    print('Digite suas 3 notas, ')
    num1 = float(input('Digite a nota número 01, ou aperte "0" para sair '))
    if num1 == 0:
        break
    num2 = int(input('Digite a nota número 02 '))
    num3 = int(input('Digite a nota número 03 '))
    m =(num1 + num2 + num3) / 3
    if m >= 60:
        print('Aprovado \n')
    elif m >= 40:
        print('Recuperação \n')
    else:
        print('Reprovado \n')
    print('Fim do cálculo')
        
print('Fim da execução do programa')