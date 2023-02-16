import random
import time
import csv
from termcolor import colored
from datetime import datetime
import sys
import codecs
import os
os.system('clear')

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


palabras = input("Introduce las palabras a utilizar, separadas por comas: ")
palabras = palabras.split(",")
conectores = ["el", "la", "los", "las", "de", "del", "a", "con", "por", "para"]

puntuacion_total = 0
numero_lineas = 0
registros = []

while True:
    linea = ""
    for i in range(random.randint(5, 10)):
        palabra = random.choice(palabras)
        if random.random() > 0.5:
            palabra = palabra.upper()
        linea += f"{palabra} {random.choice(conectores)} "
    linea = linea[:-2] + "."
    print(linea)
    inicio_tiempo = time.time()
    input_usuario = input("Escribe la línea y pulsa Enter para continuar: \n")
    fin_tiempo = time.time()
    tiempo_transcurrido = fin_tiempo - inicio_tiempo
    puntuacion_aciertos = sum([1 for palabra_correcta in linea.split() if palabra_correcta in input_usuario])
    puntuacion_tiempo = max(0, int((len(linea) / tiempo_transcurrido) / 5))
    puntuacion = puntuacion_aciertos + puntuacion_tiempo
    puntuacion_total += puntuacion
    numero_lineas += 1
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    registro = {"Fecha": fecha, "Linea": linea, "Input_usuario": input_usuario, "Puntuacion_aciertos": puntuacion_aciertos,
                "Puntuacion_tiempo": puntuacion_tiempo, "Puntuacion_total": puntuacion,
                "Tiempo_transcurrido": tiempo_transcurrido}
    registros.append(registro)
    print(f"Has obtenido {colored(puntuacion, 'green')} puntos en esta línea.")
    print(f"Tiempo transcurrido: {colored(tiempo_transcurrido, 'cyan')} segundos.")
    print(f"Puntuación total: {colored(puntuacion_total, 'yellow')} puntos en {numero_lineas} líneas.")
    guardar_progreso = input("¿Quieres guardar el progreso en un archivo CSV? (s/n): ")
    if guardar_progreso.lower() == "s":
        nombres_campos = ["Fecha", "Linea", "Input_usuario", "Puntuacion_aciertos", "Puntuacion_tiempo", "Puntuacion_total", "Tiempo_transcurrido"]
        with open("progreso.csv", mode="a", newline="") as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_campos)
            if archivo_csv.tell() == 0:
                escritor_csv.writeheader()
            for registro in registros:
                escritor_csv.writerow(registro)
        print("Progreso guardado en el archivo 'progreso.csv'.")
    registros = []

