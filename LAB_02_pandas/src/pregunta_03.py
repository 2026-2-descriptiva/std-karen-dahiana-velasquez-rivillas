def pregunta_03():
    """
    Usando `data/tbl0.tsv`, cuente cuántos registros hay para cada categoría
    de la columna `c1`. Retorne una Serie de Pandas cuyo índice son las
    categorías, en orden alfabético, y cuyos valores son las cantidades.

    Ejemplo del formato de la respuesta:

        c1
        A     8
        B     7
        C     5
        ...
    """

    import pandas as pd
    
    data = pd.read_csv(
    "data/tbl0.tsv",
    sep="\t"
    )
    
    resultado = data["c1"].value_counts().sort_index()

    return resultado

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_03()

