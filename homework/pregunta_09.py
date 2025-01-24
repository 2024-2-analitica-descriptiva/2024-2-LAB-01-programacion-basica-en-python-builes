"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



path = "files/input/data.csv"

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    d = {}

    with open(path, 'r') as file:
        data = file.readlines()

        for line in data:
            col5 = line.strip().split("\t")[4].split(",")
            for row in col5:
                val1 = row.split(":")[0]
                d[val1] = d.get(val1, 0) + 1
        return d

print(pregunta_09())