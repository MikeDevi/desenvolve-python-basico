# 05
# Lista com os livros (título, autor, ano de publicação, número de páginas)
livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
    ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
    ("1984", "George Orwell", 1949, 328),
    ("Dom Casmurro", "Machado de Assis", 1899, 256),
    ("A Revolução dos Bichos", "George Orwell", 1945, 112),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("A Menina que Roubava Livros", "Markus Zusak", 2005, 480),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223),
    ("Capitães da Areia", "Jorge Amado", 1937, 288),
    ("O Nome do Vento", "Patrick Rothfuss", 2007, 656)
]

# Criação do arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Cabeçalho
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo os dados dos livros
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")
