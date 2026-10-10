def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """

    import pandas as pd
        
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    data_melt = data["metrics"].str.split(",", expand=True).melt().dropna()
    data_melt = data_melt["value"].str.split(":", expand=True)
    data_melt.columns = ["clave", "value"]
    data_melt["value"] = pd.to_numeric(data_melt["value"])

    dict = data_melt.groupby(["clave"])["value"].agg(["min", "max"]).to_dict()

    dict_min_max = []
    for clave in sorted(dict["min"].keys()):
        min = dict["min"][clave]
        max = dict["max"][clave]
        dict_min_max.append((clave, min, max))

    return dict_min_max

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_06()
