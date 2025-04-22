# 03
def palindromo(frase):
    # Remove espaços e converte para minúsculas
    frase = frase.replace(" ", "").lower()
    # Verifica se a frase é igual à sua reversa
    return frase == frase[::-1]
while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    if frase == "Fim":
        break
    if palindromo(frase):
        print("A frase é um palíndromo.")   
    else:
        print("A frase não é um palíndromo.")