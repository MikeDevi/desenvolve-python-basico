# 03
import random

lista = [random.randint(-10,10) for _ in range(20)]

intervalos_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(lista)):
                #Início        Até o índice 19 + 1
    for m in range(i + 1, len(lista) + 1 ):
        # Separa os intervalos
        intervalo = lista[i:m]
        # Se os números do intervalo for menor que 0, o mesmo é somado na variável negativos 
        negativos = sum(1 for num in intervalo if num < 0)
        
        # Comparando os intervalos e armazendo a variavel "intervalosnegativos"
        if negativos > intervalos_negativos:
            intervalos_negativos = negativos
            inicio_intervalo = i
            fim_intervalo = m

lista_editada = lista[:inicio_intervalo] + lista[fim_intervalo:]
print(f'Lista Original: {lista}')
print(f'Lista Editada: {lista_editada}')
del lista[inicio_intervalo:fim_intervalo]
print(f'Lista aposo del: {lista}')


            
        



