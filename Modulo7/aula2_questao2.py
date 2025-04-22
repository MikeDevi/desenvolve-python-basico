# 02

vogais = 'aeiouáéíóúãõâêîôûàèìòùäëïöüåæç'
frase = input('Digite uma frase: ')
frase = frase.lower()
nova_frase = ''

for letra in frase:
    if letra in vogais:
        nova_frase  += '*'
    else:
        nova_frase += letra
print(nova_frase)

