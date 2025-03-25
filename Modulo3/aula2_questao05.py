# 05
genero = input('Digite seu genero M "Masculino" e F para "Feminino" ')
idade = int(input('Digite sua idade '))
tem_ser = int(input("Digite seu tempo de serviço "))

if genero == 'M':
    veri = idade >= 65 or tem_ser >= 30 or idade >= 60 and tem_ser >= 25
elif genero == 'F':
    veri = idade >= 60 or tem_ser >= 30 or idade >= 60 and tem_ser >= 25

print(f'Você esta apto para se aposentar? {veri}')