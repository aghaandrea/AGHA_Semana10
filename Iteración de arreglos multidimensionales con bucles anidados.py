import random

# Definir nombres de ciudades, días de la semana y semanas
nombres_ciudades = ['Ciudad Alpha', 'Ciudad Beta', 'Ciudad Cabo']
dias_de_la_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
numero_semanas = 4

# Crear matriz 3D de temperaturas
datos_temperaturas = []
    for idx_ciudad in range(len(nombres_ciudades)):
    datos_ciudad = []
    for idx_dia in range(len(dias_de_la_semana)):
    datos_dia = []
    for idx_semana in range(numero_semanas):
    temperatura_dia = random.randint(0, 40)
    datos_dia.append(temperatura_dia)
    datos_ciudad.append(datos_dia)
    datos_temperaturas.append(datos_ciudad)

# Calcular el promedio de temperaturas por ciudad y semana
for idx_ciudad, ciudad in enumerate(nombres_ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for idx_semana in range(numero_semanas):
    suma_temperaturas_semana = 0
    for idx_dia, dia in enumerate(dias_de_la_semana):
    suma_temperaturas_semana += datos_temperaturas[idx_ciudad][idx_dia][idx_semana]
    promedio_semana = suma_temperaturas_semana / len(dias_de_la_semana)
    print(f"Semana {idx_semana + 1}: {promedio_semana:.2f}°C")
    print()