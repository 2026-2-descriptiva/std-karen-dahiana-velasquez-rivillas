def pregunta_01():
    """
    El archivo `data/solicitudes_de_credito.csv.gz` contiene las solicitudes de
    un programa de crédito, pero llegó sucio: tiene una columna de índice que
    no pertenece a los datos, registros duplicados, registros incompletos y
    valores que representan lo mismo escritos de formas distintas en los
    campos de texto, las fechas, el estrato y el monto.

    Su tarea es limpiarlo y guardar el resultado en
    `submission/solicitudes_de_credito.csv`, usando punto y coma (`;`) como
    separador y sin el índice de Pandas.

    El archivo limpio debe cumplir lo siguiente:

    - Contiene solamente las nueve columnas `sexo`, `tipo_de_emprendimiento`,
      `idea_negocio`, `barrio`, `estrato`, `comuna_ciudadano`,
      `fecha_de_beneficio`, `monto_del_credito` y `línea_credito`, en ese
      orden.
    - Los campos de texto están en minúsculas y sus palabras separadas por
      espacios.
    - `estrato` y `monto_del_credito` son números enteros, sin símbolos ni
      separadores de miles.
    - Todas las fechas de `fecha_de_beneficio` usan un mismo formato, por
      ejemplo `AAAA-MM-DD`.
    - No hay registros incompletos. La única excepción es
      `comuna_ciudadano`: sus valores faltantes son parte de los datos
      originales y deben conservarse.
    - No hay registros duplicados.

    Ejemplo del formato del archivo:

        sexo;tipo_de_emprendimiento;idea_negocio;barrio;estrato;...
        femenino;comercio;almacen de ropa en;los cerros el vergel;2;...
        ...
    """

    import pandas as pd
    from pathlib import Path

    INPUT_FILE = Path("data/solicitudes_de_credito.csv.gz")
    OUTPUT_FILE = Path("submission/solicitudes_de_credito.csv")

    data = pd.read_csv(
        INPUT_FILE,
        compression="gzip",
        sep=";",
        encoding="utf-8",
        index_col=0,
    )

    cols_texto = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]
    cols_num = ["estrato", "monto_del_credito", "comuna_ciudadano"]
    cols_obligatorias = [c for c in data.columns if c != "comuna_ciudadano"]

    data[cols_texto] = data[cols_texto].apply(
      lambda s: s.str.lower().str.replace(r"[\s_\-]+", " ", regex=True).str.strip()
    )

    data[cols_num] = data[cols_num].apply(
        lambda s: pd.to_numeric(
            s.astype(str).str.replace(r"\.00$|[$,\s]", "", regex=True),
            errors="coerce",
        )
    ).astype("Int64")

    d_m_y = pd.to_datetime(data["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    y_m_d = pd.to_datetime(data["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    data["fecha_de_beneficio"] = d_m_y.fillna(y_m_d).dt.strftime("%Y-%m-%d")

    data = data.dropna(subset=cols_obligatorias).drop_duplicates()
  
    data.to_csv(OUTPUT_FILE, sep=";", index=False)


if __name__ == "__main__":
    pregunta_01()