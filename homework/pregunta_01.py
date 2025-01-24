import os

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Ruta del archivo relativa al archivo actual
relative_path = "files/input/data.csv"

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    total = 0
    

    with open(relative_path, "r") as file:
        # Leemos todas las líneas del archivo
        data = file.readlines()

        # Iteramos sobre cada línea para extraer la segunda columna y sumarla
        for line in data:
            # Separamos las columnas por comas
            column = line.strip().split(",")[0].split("\t")
            total += int(column[1])

    print(f"La suma de la segunda columna es: {total}")
    return total

print(pregunta_01())


