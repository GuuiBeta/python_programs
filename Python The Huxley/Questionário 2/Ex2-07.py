tempo = int(input())

horas = int(tempo/3600)
tempo = tempo % 3600

minutos = int(tempo/60)
tempo = tempo % 60

segundos = tempo

print(f"{horas}:{minutos}:{segundos}")