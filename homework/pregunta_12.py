"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

path = "files/input/data.csv"

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    dic = {}

    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            number = 0
            cols = line.split("\t")
            key = cols[0]
            value = cols[4].split(",")
            for row in value:
                n = int(row.split(":")[1])
                number += n
            dic[key] = dic.get(key, 0) + number
        
        return dic



print(pregunta_12())

