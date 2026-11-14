import pandas as pd
from pathlib import Path

def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """ ...tu docstring... """

    INPUT_FOLDER = Path("data")
    OUTPUT_FOLDER = Path("submission")
    OUTPUT_FOLDER.mkdir(exist_ok=True)

    data = pd.read_csv(INPUT_FOLDER / "superstore_orders.csv.gz", compression="gzip", sep=";")

    data = data.replace({",": "."}, regex=True)
    data["Profit"] = data["Profit"].astype(float)
    data["Sales"] = data["Sales"].astype(float)
    data["Discount"] = data["Discount"].astype(float)

    data["discount_band"] = pd.cut(
        data["Discount"],
        bins=[-float("inf"), 0, 0.05, 0.10, float("inf")],
        labels=["0%", "1%-5%", "6%-10%", "más de 10%"],
    )

    def profitability_summary(df):
        df = pd.DataFrame([{
            "lines": df.shape[0],
            "orders": df["Order ID"].nunique(),
            "sales": df["Sales"].sum(),
            "profit": df["Profit"].sum(),
            "profit_margin": df["Profit"].sum() / df["Sales"].sum(),
            "loss_lines": df[df["Profit"] < 0].shape[0],
            "loss_line_rate": df[df["Profit"] < 0].shape[0] / df.shape[0],
            "lost_profit": -1 * df[df["Profit"] < 0]["Profit"].sum(),
        }])
        df.to_csv(OUTPUT_FOLDER / "profitability_summary.csv", index=False)
        return df

    def discount_summary(df):
        orden = ["discount_band", "lines", "sales", "profit",
                 "profit_margin", "loss_line_rate", "lost_profit"]
        df = (
            df.assign(
                is_loss=df["Profit"] < 0,
                loss_amount=df["Profit"].clip(upper=0).abs(),
            )
            .groupby("discount_band", observed=True)
            .agg(
                lines=("Order ID", "size"),
                sales=("Sales", "sum"),
                profit=("Profit", "sum"),
                loss_lines=("is_loss", "sum"),
                lost_profit=("loss_amount", "sum"),
            )
            .assign(
                profit_margin=lambda d: d["profit"] / d["sales"],
                loss_line_rate=lambda d: d["loss_lines"] / d["lines"],
            )
            .reset_index()
        )[orden]                                   # <- reordenar ANTES de guardar
        df.to_csv(OUTPUT_FOLDER / "discount_summary.csv", index=False)
        return df

    def priority_segments(df):
        keys = ["Customer Segment", "Product Category"]
        df = (
            df.assign(
                loss_amount=df["Profit"].clip(upper=0).abs(),
                segment_lines=df.groupby(keys)["Order ID"].transform("size"),
            )
            .query("segment_lines >= 100")         # <- >= 100
            .groupby(keys)
            .agg(
                lines=("Order ID", "size"),
                sales=("Sales", "sum"),
                profit=("Profit", "sum"),
                lost_profit=("loss_amount", "sum"),
            )
            .assign(profit_margin=lambda d: d["profit"] / d["sales"])
            .reset_index()
            .sort_values("lost_profit", ascending=False)
            .head(5)                               
        )[keys + ["lines", "sales", "profit", "profit_margin", "lost_profit"]]
        df.to_csv(OUTPUT_FOLDER / "priority_segments.csv", index=False)
        return df

    return (
        profitability_summary(data),
        discount_summary(data),
        priority_segments(data),
    )

