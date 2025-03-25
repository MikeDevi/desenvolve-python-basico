# 04
classe = input('Escolha uma classe Mago, Guerreiro ou Arquiro ')
forca = int(input('Digite os pontos de força do personagem '))
magia = int(input('Digite os pontos de magia do personagem '))

if classe == "Guerreiro":
    vali = forca >= 15 and magia <= 10
elif classe == "Mago":
    vali = forca <= 10 and magia >= 15
elif classe == "Arqueiro":
    vali = 5 < forca <= 15 and 5 < magia <= 15
else:
    vali = False

print(f'Os pontos atribuidos estão consistentes com a classe escolhida? {vali}')
    