def pregunta_07():
    """
    Usando `data/tbl0.tsv`, sume los valores de la columna `c2` para cada
    categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice son
    las categorías, en orden alfabético, y cuyos valores son las sumas.

    Ejemplo del formato de la respuesta:

        c1
        A    37
        B    36
        C    27
        ...
    """

    import pandas as pd
            
    data = pd.read_csv(
    "data/tbl0.tsv",
    sep="\t"
    )

    resultado = data.groupby("c1")["c2"].sum().sort_index()

    return resultado

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_07()
