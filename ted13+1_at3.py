def converte_tempo(segundos):
    horas = segundpos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"