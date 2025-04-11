import os
import time
import datetime
import calendar

# Exibe o diretório atual
diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")

# Exibe a data e hora atuais
agora = datetime.datetime.now()
print(f"\nData e hora atuais: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# Exibe o calendário do mês atual
ano = agora.year
mes = agora.month
print(f"\nCalendário do mês {mes}/{ano}:\n")
print(calendar.month(ano, mes))

# Pausa de 3 segundos
print("Esperando 3 segundos...")
time.sleep(3)
print("Fim da pausa!")
