def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """

    import pandas as pd
    
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values("letter")

    x = data.groupby(["letter"])["letter"].count().to_dict()
    list = []
    for key, value in x.items():
        list.append((key, value))

    return list
    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_02()

