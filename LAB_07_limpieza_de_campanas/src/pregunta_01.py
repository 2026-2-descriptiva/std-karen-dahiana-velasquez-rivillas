import pandas as pd
from pathlib import Path


def tabla_client(data):
    client = data[
        ["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]
    ].copy()

    client["job"] = client["job"].str.replace(".", "", regex=False).str.replace("-", "_", regex=False)
    client["education"] = (
        client["education"].str.replace(".", "_", regex=False).replace("unknown", pd.NA)
    )
    client["credit_default"] = (client["credit_default"] == "yes").astype(int)
    client["mortgage"] = (client["mortgage"] == "yes").astype(int)

    return client


def tabla_campaign(data):
    campaign = data[
        [
            "client_id",
            "number_contacts",
            "contact_duration",
            "previous_campaign_contacts",
            "previous_outcome",
            "campaign_outcome",
        ]
    ].copy()

    campaign["previous_outcome"] = (campaign["previous_outcome"] == "success").astype(int)
    campaign["campaign_outcome"] = (campaign["campaign_outcome"] == "yes").astype(int)
    campaign["last_contact_date"] = pd.to_datetime(
        "2022-" + data["month"] + "-" + data["day"].astype(str),
        format="%Y-%b-%d",
    ).dt.strftime("%Y-%m-%d")

    return campaign


def tabla_economics(data):
    return data[["client_id", "cons_price_idx", "euribor_three_months"]].copy()


def clean_campaign_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    (docstring sin cambios)
    """

    INPUT_FOLDER = Path("data")
    OUTPUT_FOLDER = Path("submission")
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    data = pd.concat(
        (
            pd.read_csv(f, compression="gzip", encoding="utf-8", index_col=0)
            for f in sorted(INPUT_FOLDER.glob("bank-marketing-campaing-*.csv.gz"))
        ),
        ignore_index=True,
    )

    client = tabla_client(data)
    campaign = tabla_campaign(data)
    economics = tabla_economics(data)

    client.to_csv(OUTPUT_FOLDER / "client.csv", index=False)
    campaign.to_csv(OUTPUT_FOLDER / "campaign.csv", index=False)
    economics.to_csv(OUTPUT_FOLDER / "economics.csv", index=False)

    return client, campaign, economics