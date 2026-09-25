import pandas as pd

OUTPUT_FILE = "PRE_04_limpieza/submission/ventas.csv"


def main():
    df = pd.read_csv(OUTPUT_FILE)
    series = df["discount"]
    #series = series.astype(str)

    #series = series[series.str.startswith(r"COP")]
    #series = series.str.replace(r"\d", "d", regex=True)
    #series = series.drop.duplicates()

    #series = series[series.str.contains(r"-\d{2}$", regex=True)]
    # series = series[series.str.contains(r"K$", regex=True)]

    series = series.sort_values()
    series = series.drop_duplicates()

    print(series)
    print(len(series))


if __name__ == "__main__":
    main()