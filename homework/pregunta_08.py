"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Ruta del archivo relativa al archivo actual
relative_path = "files/input/data.csv"

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
                asociacion[valor_columna_2] = set()  # Usamos un set para evitar repeticiones
            asociacion[valor_columna_2].update(letras)  # Añadimos las letras asociadas
        
        # Convertimos el diccionario a una lista de tuplas, ordenando las letras y los valores
        for key in sorted(asociacion.keys()):
            resultado.append((key, sorted(list(asociacion[key]))))  # Ordenamos las letras
        
    return resultado

print(pregunta_08())