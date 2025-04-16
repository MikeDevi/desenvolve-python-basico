# 01
lista_par = [n for n in range(1,51) if n % 2 == 0 ]
print(f'Somente números pares {lista_par}')

lista_quad =[n ** 2 for n in range(1, 10)]
print(f'Valores elevados ao quadrado {lista_quad}')

lis_div_7 = [n for n in range(1, 101) if n % 7 == 0]
print(f'Valores divisíveis por 7 {lis_div_7}')

lista_par_impar = ['Par' if n % 2 == 0 else 'Impar' for n in range(0 ,30, 3)]
print(lista_par_impar)