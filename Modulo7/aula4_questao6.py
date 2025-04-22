# 06

# Abre o arquivo e analisa as músicas mais tocadas por ano (2012-2022)
arquivo = "spotify-2023.csv"
musicas_por_ano = {}

with open(arquivo, "r", encoding="latin-1") as f:
    # Lê todas as linhas ignorando o cabeçalho
    linhas = f.readlines()[1:]

    for linha in linhas:
        # Ignora linhas que contém aspas (casos especiais com vírgula dentro dos campos)
        if '"' in linha:
            continue

        dados = linha.strip().split(',')

        try:
            # Extrai os campos necessários
            track_name = dados[0]
            artist_name = dados[1]
            artist_count = int(dados[2])
            year = int(dados[3])
            streams = int(dados[8])
        except (IndexError, ValueError):
            continue  # pula linhas malformadas

        # Filtra apenas anos entre 2012 e 2022
        if 2012 <= year <= 2022:
            # Se ainda não temos música para esse ano, adicionamos
            if year not in musicas_por_ano:
                musicas_por_ano[year] = [track_name, artist_name, year, streams]
            else:
                # Substitui se esta tiver mais streams que a atual armazenada
                if streams > musicas_por_ano[year][3]:
                    musicas_por_ano[year] = [track_name, artist_name, year, streams]

# Gera a lista final ordenada por ano
resultado = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]

# Exibe o resultado
for musica in resultado:
    print(musica)
