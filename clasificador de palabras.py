import csv
import nltk
from nltk.corpus import opinion_lexicon
from nltk.corpus import wordnet
import os
import tkinter as tk
from tkinter import filedialog

# Descargar recursos de NLTK
nltk.download('opinion_lexicon')
nltk.download('wordnet')

# Cargar listas de palabras positivas y negativas de NLTK
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

# Función para seleccionar el archivo CSV
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo CSV del diccionario",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    return archivo

# Función para clasificar palabras según el sentimiento
def clasificar_palabras(archivo_csv):
    resultados_clasificados = []

    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la cabecera

        for row in reader:
            palabra = row[0]
            frecuencia = row[1]
            if palabra in positive_words:
                sentimiento = "Positiva"
            elif palabra in negative_words:
                sentimiento = "Negativa"
            else:
                sentimiento = "Neutral"
            
            resultados_clasificados.append([palabra, frecuencia, sentimiento])

    # Guardar los resultados en un nuevo archivo CSV
    nombre_salida = os.path.splitext(archivo_csv)[0] + "_clasificado.csv"
    with open(nombre_salida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Palabra", "Frecuencia", "Sentimiento"])
        writer.writerows(resultados_clasificados)

    print(f"Archivo clasificado guardado en '{nombre_salida}'.")

# Ejecutar el programa
archivo_csv = seleccionar_archivo()
if archivo_csv:
    clasificar_palabras(archivo_csv)
else:
    print("No se seleccionó ningún archivo.")
