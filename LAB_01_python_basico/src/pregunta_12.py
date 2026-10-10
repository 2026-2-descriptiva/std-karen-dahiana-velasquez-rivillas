def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """

    import pandas as pd

    data = pd.read_csv(
    "data/data.csv.gz",
    compression="gzip",
    sep="\t",         
    header=None,
    names = ["letter", "value", "date","codes", "metrics"]
    ).sort_values("letter")

    data["metrics_list"] = data["metrics"].str.split(",")
    df_exploded = data.explode("metrics_list")
    df_exploded[["metric", "metric_value"]] = df_exploded["metrics_list"].str.split(":", expand=True)
    df_exploded["metric_value"] = df_exploded["metric_value"].astype(int)
    result  = df_exploded.groupby("letter")["metric_value"].agg("sum").to_dict()

    return result

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_12()
