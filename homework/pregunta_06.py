from collections import defaultdict

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Ruta del archivo relativa al archivo actual
relative_path = "../files/input/data.csv"

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    

    # Diccionario para acumular los valores de cada clave
    valores = defaultdict(list)

    # Leer el archivo línea por línea
    with open(relative_path, "r") as f:
        for line in f:
            # Extraer la columna 5
            columna_5 = line.strip().split("\t")[4]
            # Dividir en pares clave:valor
            pares = columna_5.split(",")
            for par in pares:
                clave, valor = par.split(":")
                valores[clave].append(int(valor))

    # Calcular el mínimo y máximo para cada clave
    resultado = []
    for clave, lista_valores in sorted(valores.items()):
        resultado.append((clave, min(lista_valores), max(lista_valores)))

    return resultado

print(pregunta_06())
