def pregunta_06():
    """
    Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
    conviértalos a mayúsculas y retórnelos como una lista ordenada
    alfabéticamente.

    Ejemplo del formato de la respuesta:

        ["A", "B", "C", "D", "E", "F", "G"]
    """

    import pandas as pd
                
    data = pd.read_csv(
    "data/tbl1.tsv",
    sep="\t"
    )

    resultado = list(data["c4"].sort_values().str.upper().unique())

    return resultado

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_06()
