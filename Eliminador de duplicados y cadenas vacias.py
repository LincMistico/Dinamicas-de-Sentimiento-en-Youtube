import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

# Función para cargar un archivo .csv mediante el explorador de archivos
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo CSV",
        filetypes=[("CSV files", "*.csv")]
    )
    return file_path

# Función principal para limpiar el archivo
def limpiar_comentarios_csv():
    archivo = seleccionar_archivo()
    
    if not archivo:
        print("No se seleccionó ningún archivo.")
        return
    
    # Cargar el archivo CSV
    df = pd.read_csv(archivo)

    # Asegurarse de que la columna de comentarios exista
    if 'Comentario' not in df.columns:
        print("La columna 'Comentario' no existe en el archivo.")
        return

    # Eliminar duplicados en la columna 'Comentario'
    df = df.drop_duplicates(subset=['Comentario'])

    # Eliminar filas donde los comentarios sean NA o estén vacíos
    df = df.dropna(subset=['Comentario'])
    df = df[df['Comentario'].str.strip() != ""]

    # Guardar el archivo limpio en un nuevo archivo CSV
    archivo_limpio = os.path.splitext(archivo)[0] + "_limpio.csv"
    df.to_csv(archivo_limpio, index=False)
    print(f"Archivo limpio guardado como: {archivo_limpio}")

# Ejecutar la función
limpiar_comentarios_csv()
