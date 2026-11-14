import pandas as pd
import numpy as np

def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Una entidad pública recibe peticiones, quejas, reclamos y sugerencias
    (PQRS) por dos canales, la página web y las cartas, y la ley le da 15 días
    hábiles para responder cada una. Su tarea es medir si la entidad cumple
    ese plazo.

    Los archivos `data/historical_requests_web.csv.gz` y
    `data/historical_requests_letter.csv.gz` tienen una fila por solicitud
    recibida entre 2016 y 2021 por cada canal, con su identificador
    (`record_id`), la fecha de entrada (`in_date`), el día de la semana de
    entrada (`day_name`) y la fecha de respuesta (`out_date`). Si `out_date`
    está vacía, la solicitud todavía no ha sido respondida.

    Tenga en cuenta lo siguiente:

    - Algunas solicitudes aparecen repetidas: elimine las filas idénticas
      dentro de cada canal, para contar cada solicitud una sola vez. Las
      filas sin `record_id` son solicitudes válidas.
    - Llame `letter` al canal de las cartas y `web` al de la página web.
    - Los días hábiles de respuesta son los días de lunes a viernes
      posteriores a la fecha de entrada, hasta la fecha de respuesta
      incluida. Por ejemplo, una solicitud que entra un viernes y se responde
      el lunes siguiente tardó 1 día hábil. No considere los festivos.
    - Los días calendario de respuesta son la diferencia entre la fecha de
      respuesta y la de entrada.
    - Una solicitud cumple el plazo si fue respondida en 15 días hábiles o
      menos. Una solicitud pendiente no ha cumplido el plazo.
    - `on_time_rate` es la proporción de solicitudes que cumplen el plazo,
      sobre el total de solicitudes, incluidas las pendientes.
    - Las medianas de días se calculan solamente con las solicitudes
      respondidas.

    Genere tres archivos en `submission/`, sin el índice de Pandas y con las
    columnas en el orden indicado:

    1. `channel_summary.csv`, con una fila por canal, en orden alfabético:
       `channel`, `requests`, `answered`, `pending`,
       `median_business_days` y `on_time_rate`.

    2. `yearly_summary.csv`, con una fila por año de entrada y canal,
       ordenada por año y luego por canal: `year`, `channel`, `requests`,
       `pending` y `on_time_rate`.

    3. `entry_day_summary.csv`, con una fila por día de entrada, de lunes a
       domingo, con los dos canales juntos: `day_name`, `requests`,
       `median_calendar_days` y `median_business_days`.

    Observe en el tercer archivo cómo cambia la lectura del tiempo de
    respuesta según se cuenten días calendario o días hábiles.

    La función también debe retornar las tres tablas, en el mismo orden.

    Ejemplo del formato de `channel_summary.csv`:

        channel,requests,answered,pending,median_business_days,on_time_rate
        letter,28138,...
        ...
    """

    festivos = [
    # 2016
    "2016-01-01", "2016-01-11", "2016-03-21", "2016-03-24", "2016-03-25",
    "2016-05-01", "2016-05-09", "2016-05-30", "2016-06-06", "2016-07-04",
    "2016-07-20", "2016-08-07", "2016-08-15", "2016-10-17", "2016-11-07",
    "2016-11-14", "2016-12-08", "2016-12-25",
    # 2017
    "2017-01-01", "2017-01-09", "2017-03-20", "2017-04-13", "2017-04-14",
    "2017-05-01", "2017-05-29", "2017-06-19", "2017-06-26", "2017-07-03",
    "2017-07-20", "2017-08-07", "2017-08-21", "2017-10-16", "2017-11-06",
    "2017-11-13", "2017-12-08", "2017-12-25",
    # 2018
    "2018-01-01", "2018-01-08", "2018-03-19", "2018-03-29", "2018-03-30",
    "2018-05-01", "2018-05-14", "2018-06-04", "2018-06-11", "2018-07-02",
    "2018-07-20", "2018-08-07", "2018-08-20", "2018-10-15", "2018-11-05",
    "2018-11-12", "2018-12-08", "2018-12-25",
    # 2019
    "2019-01-01", "2019-01-07", "2019-03-25", "2019-04-18", "2019-04-19",
    "2019-05-01", "2019-06-03", "2019-06-24", "2019-07-01", "2019-07-20",
    "2019-08-07", "2019-08-19", "2019-10-14", "2019-11-04", "2019-11-11",
    "2019-12-08", "2019-12-25",
    # 2020
    "2020-01-01", "2020-01-06", "2020-03-23", "2020-04-09", "2020-04-10",
    "2020-05-01", "2020-05-25", "2020-06-15", "2020-06-22", "2020-06-29",
    "2020-07-20", "2020-08-07", "2020-08-17", "2020-10-12", "2020-11-02",
    "2020-11-16", "2020-12-08", "2020-12-25",
    # 2021
    "2021-01-01", "2021-01-11", "2021-03-22", "2021-04-01", "2021-04-02",
    "2021-05-01", "2021-05-17", "2021-06-07", "2021-06-14", "2021-07-05",
    "2021-07-20", "2021-08-07", "2021-08-16", "2021-10-18", "2021-11-01",
    "2021-11-15", "2021-12-08", "2021-12-25",
    ]

    cols = ["in_date", "out_date"]

    web = pd.read_csv("data/historical_requests_web.csv.gz", compression='gzip', sep=',')
    web["channel"] = "web"

    letter = pd.read_csv("data/historical_requests_letter.csv.gz", compression='gzip', sep=',')
    letter["channel"] = "letter"

    df_request = pd.concat([web, letter]).drop_duplicates()
    df_request = df_request.reset_index(drop=True)

    df_request[cols] = df_request[cols].apply(pd.to_datetime, format="%Y-%m-%d")
    df_request["calendar_days"] = (df_request["out_date"] - df_request["in_date"]).dt.days
    df_request["year"] = df_request["in_date"].dt.year

    ok = df_request["in_date"].notna() & df_request["out_date"].notna()

    df_request["business_days"] = pd.array([pd.NA] * len(df_request), dtype="Int64")
    df_request.loc[ok, "business_days"] = np.busday_count(
        (df_request.loc[ok, "in_date"] + pd.Timedelta(days=1)).values.astype("datetime64[D]"),
        (df_request.loc[ok, "out_date"] + pd.Timedelta(days=1)).values.astype("datetime64[D]"),
    )

  

    channel_summary = (
        df_request.groupby("channel")
          .agg(
              requests=("record_id", "size"),
              answered=("out_date", "count"),
              pending=("out_date", lambda x: x.isna().sum()),
              median_business_days=("business_days", "median"),
              on_time_rate=("business_days", lambda x: (x <= 15).sum() / x.size),
          )
          .reset_index()
    ).sort_values("channel")

    channel_summary.to_csv("submission/channel_summary.csv",index=False)

    yearly_summary = (
      df_request.groupby(["year", "channel"]).agg(
      requests=("record_id", "size"),
      pending=("out_date", lambda x: x.isna().sum()),
      on_time_rate=("business_days", lambda x: (x <= 15).sum() / x.size),
    ).reset_index()
    ).sort_values(["year", "channel"])

    yearly_summary.to_csv("submission/yearly_summary.csv",index=False)

    orden = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    entry_day_summary = (
        df_request.groupby("day_name")
          .agg(
              requests=("record_id", "size"),
              median_calendar_days=("calendar_days", "median"),
              median_business_days=("business_days", "median"),
          )
          .reindex(orden)
          .reset_index()
    )

    entry_day_summary.to_csv("submission/entry_day_summary.csv",index=False)

    #raise NotImplementedError

    return channel_summary, yearly_summary, entry_day_summary

if __name__ == "__main__":
    pregunta_01()