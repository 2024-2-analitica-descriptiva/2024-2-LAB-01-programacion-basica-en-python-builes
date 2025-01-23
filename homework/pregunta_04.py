"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Ruta del archivo relativa al archivo actual
relative_path = "../files/input/data.csv"

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    with open(relative_path, "r") as file:
        # Leemos todas las líneas del archivo
        data = file.readlines()

        d = {}

        # Iteramos sobre cada línea para extraer la segunda columna y sumarla
        for line in data:
            # Separamos las columnas por comas
            column = line.strip().split(",")[0].split("\t")
            month = column[2].split("-")[1]
            d[month] = d.get(month, 0) + 1
        return sorted(d.items())

print(pregunta_04())
