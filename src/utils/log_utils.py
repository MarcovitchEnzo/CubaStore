import os
from datetime import datetime


def registrar_log(mensagem):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    data_hora = datetime.now()
    texto_completo = str(data_hora) + " - " + mensagem
    with open('logs/pipeline.log', 'a') as log:
        log.write(texto_completo + "\n")