def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.

    Ejemplo del formato de la respuesta:

        [("01", 3), ("02", 4), ("03", 2), ...]
    """

    import pandas as pd
            
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    data["month"] = data["date"].str.split("-").str[1]

    conteo = data["month"].value_counts().sort_index()
    data = data.sort_values("month")

    resultado = list(conteo.items())

    return resultado

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_04()