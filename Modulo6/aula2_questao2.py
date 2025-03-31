# 02
import random

num_elementos = random.randint(5, 20)
elementos = []
n = 0 
while n <= num_elementos:
    num_elem = random.randint(1, 10)
    elementos.append(num_elem)
    n += 1
    
print(f'A lista original: {elementos}')
print(f'A lista soma: {sum(elementos)}')
print(f'A lista media: {sum((elementos)) / len(elementos)}')
