def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """

    import pandas as pd
            
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    )

    data_melt = data["metrics"].str.split(",", expand=True).melt().dropna()
    data_melt = data_melt["value"].str.split(":", expand=True)
    data_melt.columns = ["clave", "value"]

    data_melt = data_melt.drop(["value"], axis=1).sort_values("clave")
    conteo = data_melt["clave"].value_counts(sort = False).to_dict()
    
    return conteo

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_09()
