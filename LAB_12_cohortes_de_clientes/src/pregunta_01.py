import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def build_cohort_analysis() -> pd.DataFrame:
    """
    Una tienda quiere saber si sus clientes vuelven a comprar después de su
    primera compra. Para responder, agrupe a los clientes en cohortes según
    el mes de su primera compra y mida, mes a mes, qué proporción de cada
    cohorte vuelve a comprar. Use `data/sales.csv.gz`, que tiene una fila por
    orden con su cliente (`CustomerID`) y su fecha (`OrderDate`).

    Use estas definiciones:

    - `cohort_month`: el mes de la primera compra del cliente, escrito como
      `AAAA-MM`.
    - `period_index`: los meses transcurridos desde `cohort_month`; es 0 en el
      mes de la primera compra, 1 en el mes siguiente, y así sucesivamente.
    - `active_customers`: la cantidad de clientes distintos de la cohorte que
      compraron en ese período.
    - `cohort_size`: la cantidad de clientes de la cohorte, es decir, sus
      clientes activos en el período 0.
    - `retention_rate`: `active_customers` sobre `cohort_size`.

    Genere dos archivos en `submission/`:

    1. `cohort_retention.csv`, sin el índice de Pandas, con las columnas
       `cohort_month`, `period_index`, `active_customers`, `cohort_size` y
       `retention_rate`, y una fila por cada combinación cohorte–período
       observada, ordenadas por cohorte y período.

    2. `cohort_retention_heatmap.png`, un mapa de calor de `retention_rate`
       con una fila por cohorte (eje vertical) y una columna por período
       (eje horizontal). Muestre los valores como porcentajes. Los períodos
       que todavía no se pueden observar para una cohorte no significan
       retención cero: déjelos vacíos en el mapa.

    La función también debe retornar la tabla de retención.

    Ejemplo del formato de `cohort_retention.csv`:

        cohort_month,period_index,active_customers,cohort_size,retention_rate
        2022-01,0,100,100,1.0
        2022-01,1,26,100,0.26
        ...
    """

    data = pd.read_csv('data/sales.csv.gz', compression='gzip')

    data["OrderDate"] = pd.to_datetime(data["OrderDate"])

    data["cohort_month"] = (
        data.groupby("CustomerID")["OrderDate"].transform("min").dt.to_period("M")
    )

    data["period_index"] = (
    data["OrderDate"].dt.month - data["cohort_month"].dt.month
    )

    cohort_size = data[data["period_index"] == 0].groupby("cohort_month").agg(
    cohort_size=("CustomerID", "nunique")
)

    cohort_retention = data.groupby(["cohort_month", "period_index"], as_index=False).agg(
        active_customers=("CustomerID", "nunique")
    ).sort_values(["cohort_month", "period_index"])

    cohort_retention = cohort_retention.merge(cohort_size, on="cohort_month")

    cohort_retention["retention_rate"] = (
        cohort_retention["active_customers"] / cohort_retention["cohort_size"]
    )
    cohort_retention = cohort_retention[["cohort_month", "period_index", "active_customers", "cohort_size", "retention_rate"]]
    cohort_retention.to_csv("submission/cohort_retention.csv", index=False)



    cohort_retention_heatmap_df = cohort_retention.copy()
    cohort_retention_heatmap_df["retention_rate"] = cohort_retention["retention_rate"] * 100 

    cohort_retention_heatmap = cohort_retention_heatmap_df.pivot(
        index="period_index", columns="cohort_month", values="retention_rate"
    )

    fig, ax = plt.subplots()
    ax = sns.heatmap(cohort_retention_heatmap, annot=True, fmt=".2f", ax=ax)

    ax.set_xlabel("Cohort month")
    ax.set_ylabel("Period index")
    ax.set_title("Retention rate by cohort month and period index")
    fig.savefig("submission/cohort_retention_heatmap.png")

    return cohort_retention

    #raise NotImplementedError
