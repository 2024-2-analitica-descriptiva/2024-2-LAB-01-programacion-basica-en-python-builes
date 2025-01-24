"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Ruta del archivo relativa al archivo actual
relative_path = "files/input/data.csv"

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    resultado = []
    
    # Leemos el archivo data.csv
    with open(relative_path, 'r') as f:
        # Saltamos el encabezado
        next(f)
        
        # Creamos un diccionario para almacenar las letras asociadas a cada valor de la columna 2
        asociacion = {}
        
        # Iteramos sobre cada línea del archivo
        for line in f:
            columnas = line.strip().split('\t')
            
            # Extraemos las columnas 1 y 2
            letras = columnas[0]
            valor_columna_2 = int(columnas[1])  # Convertimos el valor de la columna 2 a entero
            
            # Si el valor de la columna 2 ya está en el diccionario, agregamos las letras
            if valor_columna_2 not in asociacion:
                asociacion[valor_columna_2] = []
            asociacion[valor_columna_2].append(letras)
        
        # Convertimos el diccionario a una lista de tuplas
        for key in sorted(asociacion.keys()):
            resultado.append((key, asociacion[key]))
    
    return resultado

print(pregunta_07())