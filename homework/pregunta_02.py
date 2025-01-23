"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Ruta del archivo relativa al archivo actual
relative_path = "../files/input/data.csv"

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    d = {}

    with open(relative_path, "r") as file:
        # Leemos todas las líneas del archivo
        data = file.readlines()

        # Iteramos sobre cada línea para extraer la segunda columna y sumarla
        for line in data:
            # Separamos las columnas por comas
            column = line.strip().split(",")[0].split("\t")
            current = column[0]

            d[current] = d.get(current, 0) + 1
        return d
print(pregunta_02())
