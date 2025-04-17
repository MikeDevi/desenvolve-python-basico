# 08

def valida_cpf(cpf: str):
    # Remove pontos e hífen
    cpf_numeros = cpf.replace('.', '').replace('-', '')

    # Verifica se tem 11 dígitos numéricos
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        print("Formato inválido")
        return

    # Converte em lista de inteiros
    numeros = [int(d) for d in cpf_numeros]

    # Cálculo do primeiro dígito verificador
    soma1 = sum(n * m for n, m in zip(numeros[:9], range(10, 1, -1)))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    # Cálculo do segundo dígito verificador
    soma2 = sum(n * m for n, m in zip(numeros[:9] + [digito1], range(11, 1, -1)))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    # Verifica se os dígitos calculados batem com os fornecidos
    if numeros[9] == digito1 and numeros[10] == digito2:
        print("Válido")
    else:
        print("Inválido")
