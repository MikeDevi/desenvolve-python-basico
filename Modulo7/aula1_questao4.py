# 04
numero = input('Digite um número: ')
if len(numero) == 8:
    numero = '9' + numero
if '9' in numero[0]:
    novo_numero = numero[:1] + '-' + numero [1:]
    
print(f'O número formatado é: {novo_numero}')
    
    
    