def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """

    import pandas as pd

    data = pd.read_csv(
    "data/tbl0.tsv",
    sep="\t"
    )

    #raise NotImplementedError

    return data.shape[0]

if __name__ == "__main__":
    pregunta_01()
