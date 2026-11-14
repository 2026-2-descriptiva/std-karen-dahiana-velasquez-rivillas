def pregunta_13():
    """
    Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
    `c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
    para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
    índice son las categorías, en orden alfabético, y cuyos valores son las
    sumas.

    Ejemplo del formato de la respuesta:

        c1
        A    146
        B    134
        C     81
        ...
    """
    import pandas as pd

    data_l0 = pd.read_csv("data/tbl0.tsv", sep="\t")
    data_l2 = pd.read_csv("data/tbl2.tsv", sep="\t")

    union = pd.merge(data_l0, data_l2, on="c0")
    resultado = union.groupby("c1")["c5b"].sum().sort_index()

    return resultado

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_13()