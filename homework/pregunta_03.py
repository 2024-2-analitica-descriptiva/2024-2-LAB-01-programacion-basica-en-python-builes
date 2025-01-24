"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Ruta del archivo relativa al archivo actual
relative_path = "files/input/data.csv"

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    d = {}

    with open(relative_path, "r") as file:
        # Leemos todas las líneas del archivo
        data = file.readlines()

        # Iteramos sobre cada línea para extraer la segunda columna y sumarla
        for line in data:
            # Separamos las columnas por comas
            column = line.strip().split(",")[0].split("\t")
            key = column[0]
            value = int(column[1])

            d[key] = d.get(key, 0) + value

        # Convertimos el diccionario en una lista de tuplas ordenada alfabéticamente
        return sorted(d.items())
    
print(pregunta_03())
