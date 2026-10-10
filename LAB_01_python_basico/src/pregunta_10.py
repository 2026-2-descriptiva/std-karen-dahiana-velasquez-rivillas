def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """

    import pandas as pd

    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    data["count_metrics"] = data["metrics"].str.split(",").apply(len)
    data["count_codes"] = data["codes"].str.split(",").apply(len)

    tuplas = []
    for _,row in data.iterrows():
        tuplas.append((row["letter"], row["count_codes"], row["count_metrics"]))

    return tuplas

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_10()
