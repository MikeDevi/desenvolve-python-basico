# 01
data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
# unpacking    
dia, mes, ano = data_nasc.split("/")
# Transformando o mês em inteiro
mes =int(mes)
# Indice do mês - 1
mes = meses[mes - 1]
print(f"Você nasceu em {dia} de {mes} de {ano}.")

