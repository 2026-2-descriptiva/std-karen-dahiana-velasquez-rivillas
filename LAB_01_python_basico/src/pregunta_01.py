def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """

    import pandas as pd

    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    result = data["value"].sum()

    return result

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_01()
