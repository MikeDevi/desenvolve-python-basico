#04
from datetime import datetime

hr_agora = datetime.now()
dt_agr_formatada = hr_agora.strftime('%d/%m/%Y %H:%M')
print(f'Data atual: {dt_agr_formatada}')