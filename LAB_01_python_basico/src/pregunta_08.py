def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """

    import pandas as pd
                
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values(["value", "letter"])

    count = data.groupby("value")["letter"].agg(lambda x: [v for v in x.unique()])
    lista_tuplas = [(idx, val) for idx, val in zip(count.index, count.values)]

    return lista_tuplas

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_08()
