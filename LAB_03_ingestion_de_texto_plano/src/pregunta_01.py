import pandas as pd
import re

def pregunta_01():
    """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
    """

    with open("data/clusters_report.txt") as f:
        lineas = f.readlines()

    datos = []
    actual = None  

    for linea in lineas:
        match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)", linea)

        if match:
            if actual is not None:
                datos.append(actual)
            cluster, cantidad, porcentaje, resto = match.groups()
            actual = {
                "cluster": int(cluster),
                "cantidad_de_palabras_clave": int(cantidad),
                "porcentaje_de_palabras_clave": float(porcentaje.replace(",", ".")),
                "texto": resto.strip(),
            }
        elif actual is not None and linea.strip() and "---" not in linea:
            actual["texto"] += " " + linea.strip()

    if actual is not None:
        datos.append(actual)

    for d in datos:
      texto = " ".join(d.pop("texto").split()).rstrip(".")
      palabras = [p.strip() for p in texto.split(",")]
      d["principales_palabras_clave"] = ", ".join(p for p in palabras if p)

    return pd.DataFrame(datos)
