# 02

frase = input('Digite uma frase: ')
vogais_list = list(['a','e', 'i','o','u'])
vogais = sorted([letra.lower() for letra in frase if letra.lower() in vogais_list])
consoantes = sorted([letra for letra in frase if letra.isalpha() and letra.lower() not in vogais_list])
print('Vogais:', vogais)
print('Consoantes:', consoantes)





            
        



