def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """

    import pandas as pd
        
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values("letter")
    
    list = []
    x = data.groupby(["letter"])["value"].sum().to_dict()
    for key, value in x.items():
        list.append((key, value))

    return list
    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_03()