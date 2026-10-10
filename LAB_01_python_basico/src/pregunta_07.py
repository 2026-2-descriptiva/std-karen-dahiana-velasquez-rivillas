def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """

    import pandas as pd
            
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    count = data.groupby("value")["letter"].agg(lambda x: [v for v in x])
    lista_tuplas = [(idx, val) for idx, val in zip(count.index, count.values)]

    return lista_tuplas

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_07()
