# 03    
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(hr, 40) + ganho_por_hora * max(0, hr - 40) for hr in horas_trabalhadas]  

print('Pagammentos: ', pagamentos)

