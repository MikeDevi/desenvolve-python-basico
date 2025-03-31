# 04
def intercalar_listas(lista1, lista2):
    lista_combinada = []
    tamanho_minimo = min(len(lista1), len(lista2))
    
    for i in range(tamanho_minimo):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])
    
    if len(lista1) > len(lista2):
        lista_combinada.extend(lista1[tamanho_minimo:])
    else:
        lista_combinada.extend(lista2[tamanho_minimo:])
    
    return lista_combinada

lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))

lista_combinada = intercalar_listas(lista1, lista2)

print(f'A lista combinada é: {lista_combinada}')
