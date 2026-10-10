def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """

    import pandas as pd
    
    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values("letter")

    data["codes_list"] = data["codes"].str.split(",")
    df_exploded = data.explode("codes_list")
    result = df_exploded.groupby(["codes_list"])["value"].agg("sum").to_dict()

    return result
    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_11()
