def pregunta_01():
    """
    Las frases de este laboratorio no están en una tabla, sino en miles de
    archivos de texto organizados en carpetas. Dentro de `data/` hay dos
    carpetas, `train/` y `test/`, y cada una contiene las carpetas
    `negative/`, `neutral/` y `positive/`. Cada archivo `.txt` contiene una
    frase, y la carpeta donde se encuentra indica su sentimiento.

    Su tarea es construir un dataset para cada división y guardarlo en:

    - `submission/train_dataset.csv`
    - `submission/test_dataset.csv`

    Cada archivo debe tener dos columnas: `phrase`, con el texto de la frase,
    y `target`, con el nombre de la carpeta de sentimiento (`negative`,
    `neutral` o `positive`). Recorra las carpetas y los archivos en orden
    alfabético, de modo que el resultado sea siempre el mismo. No guarde el
    índice de Pandas en el CSV.

    Ejemplo del formato de cada archivo:

        phrase,target
        "The real estate company posted a net loss ...",negative
        ...
        "Cardona slowed her vehicle , turned around ...",neutral
        ...
    """

    import pandas as pd
    from pathlib import Path
    import os

    input_folder = Path("data")
    output_folder = Path("submission")
    carpeta_train = input_folder / "train"
    carpeta_test = input_folder / "test"

    data_output = []

    for carpeta in [carpeta_train, carpeta_test]:
        name = carpeta.name
        for subcarpeta in ["negative", "neutral", "positive"]:
            ruta_subcarpeta = carpeta/ subcarpeta
            for archivo in sorted(os.listdir(ruta_subcarpeta)):
                ruta_archivo = ruta_subcarpeta / archivo

                if ruta_archivo.is_file():
                    with open(ruta_archivo, "r", encoding="utf-8") as f:
                        contenido = f.read().strip()

                    data_output.append({
                        "source": name,
                        "phrase": contenido,
                        "target": subcarpeta,
                    })

    df = pd.DataFrame(data_output)

    train_dataset = df[df["source"] == "train"].drop("source", axis=1)
    train_dataset.to_csv(output_folder/ "train_dataset.csv", index=False)

    test_dataset = df[df["source"] == "test"].drop("source", axis=1)
    test_dataset.to_csv(output_folder/ "test_dataset.csv", index=False)

    #raise NotImplementedError

if __name__ == "__main__":
    pregunta_01()
