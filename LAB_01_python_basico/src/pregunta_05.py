def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """

    import pandas as pd
            
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values("letter")

    dict = data.groupby(["letter"])["value"].agg(["min", "max"]).to_dict()

    dict_min_max = []
    for letra in data["letter"].unique():
        max = dict["max"][letra]
        min = dict["min"][letra]
        dict_min_max.append((letra, max, min))

    return dict_min_max
    #raise NotImplementedError


if __name__ == "__main__":
    pregunta_05()