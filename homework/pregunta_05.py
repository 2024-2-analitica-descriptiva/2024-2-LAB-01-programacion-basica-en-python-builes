"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Ruta del archivo relativa al archivo actual
relative_path = "files/input/data.csv"

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    # Diccionario para almacenar los valores de la columna 2 por cada letra
    d = {}

    with open(relative_path, "r") as file:
        # Leer todas las líneas del archivo
        data = file.readlines()

        # Iterar sobre las líneas
        for line in data:
            # Dividir la línea por tabulaciones
            columns = line.strip().split(",")[0].split("\t")
            letter = columns[0]  # Columna 1 (letra)
            value = int(columns[1])  # Columna 2 (número)

            # Actualizar el diccionario con valores máximos y mínimos
            if letter not in d:
                d[letter] = [value, value]  # [máximo, mínimo]
            else:
                d[letter][0] = max(d[letter][0], value)  # Actualizar máximo
                d[letter][1] = min(d[letter][1], value)  # Actualizar mínimo

    # Convertir el diccionario en una lista de tuplas
    result = [(key, d[key][0], d[key][1]) for key in sorted(d.keys())]
    return result

print(pregunta_05())