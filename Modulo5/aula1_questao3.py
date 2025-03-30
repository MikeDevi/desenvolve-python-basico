#03
import random

while True:
    print('Adivinhe um número que será printado de 1 a 5')
    num = int(input('Digite o seu palpite: '))
    aleatorios = random.randint(0, 5)
    print(aleatorios)
    if num == aleatorios:
        print('Parandens vc acertou!!')
        break
    else:
        print(f'Valor digitado {num} \n Valor gerado {aleatorios} \n Tente novamente!!')