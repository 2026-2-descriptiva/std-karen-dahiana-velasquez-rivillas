def pregunta_02():
    """
    ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        4
    """
    import pandas as pd

    data = pd.read_csv(
    "data/tbl0.tsv",
    sep="\t"
    )

    #raise NotImplementedError

    return data.shape[1]

if __name__ == "__main__":
    pregunta_02()