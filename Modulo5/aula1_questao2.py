#02
import random
import math

n = int(input('Digite um número'))
# "_" é uma variável dummy ou place holder, usada quando o valor da variavel não é importante
aleatorio = [random.randint(0, 100) for _ in range(n)]
soma = sum(aleatorio)

raiz = math.sqrt(soma)

print('Números aleatórios gerafos', aleatorio)
print('A somo dos números é: ', soma)
print('A Raiz gos números aleatórios são: ', raiz)