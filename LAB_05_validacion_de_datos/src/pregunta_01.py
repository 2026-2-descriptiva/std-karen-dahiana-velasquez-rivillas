import pandas as pd
import json
import numpy as np

def main():
    """
    Antes de limpiar o analizar un conjunto de datos, un analista debe
    documentar qué problemas tiene. En este laboratorio usted no va a limpiar
    `data/ventas.csv.gz`: va a construir un reporte de calidad que deje evidencia
    de sus problemas, tal como están en el archivo.

    Lea `data/ventas.csv.gz` sin modificar sus valores. Para trabajar con los
    encabezados, normalícelos: páselos a minúsculas, elimine los espacios al
    inicio y al final (y cualquier marca BOM) y reemplace los espacios
    internos por `_`. Las columnas requeridas son `supplier_id`, `supplier`,
    `country`, `city`, `purchase_date`, `amount`, `discount`, `weight`,
    `units`, `unit_price` y `contact_email`.

    Escriba el reporte en `submission/data_quality_report.json` con estas
    claves:

    - `row_count`: cantidad de filas de datos.
    - `column_count`: cantidad de columnas.
    - `missing_required_columns`: lista ordenada de columnas requeridas que no
      están en el archivo.
    - `unexpected_columns`: lista ordenada de columnas del archivo que no son
      requeridas.
    - `duplicate_row_count`: cantidad de filas idénticas a una fila anterior.
    - `duplicate_supplier_id_row_count`: cantidad de filas cuyo `supplier_id`
      aparece más de una vez (cuente todas esas filas, no solo las
      repetidas).
    - `missing_value_count_by_column`: diccionario con la cantidad de valores
      faltantes de cada columna. Considere faltantes las celdas vacías y las
      que contienen `N/A`.
    - `invalid_email_count`: cantidad de valores de `contact_email` que no
      tienen la forma `usuario@dominio.extension`.
    - `invalid_unit_count`: cantidad de valores numéricos de `units` que no son
      enteros positivos. Los valores faltantes no se cuentan aquí.
    - `country_values`: lista ordenada de los valores distintos de `country`,
      escritos exactamente como aparecen en el archivo.

    La función también debe retornar el reporte como un diccionario.

    Ejemplo del formato del reporte:

        {
          "row_count": 103,
          "column_count": 11,
          "missing_required_columns": [],
          ...
          "country_values": [" Colombia ", "CO", ...]
        }
    """

    data = pd.read_csv('data/ventas.csv.gz', compression='gzip') 
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

    columnas_requeridas = ['supplier_id', 'supplier','country', 'city', 'purchase_date', 'amount', 'discount', 'weight','units', 'unit_price','contact_email']

    result = {
        "row_count" : data.shape[0],
        "column_count" : data.shape[1],
        "missing_required_columns" : [col for col in columnas_requeridas if col not in data.columns],
        "unexpected_columns" : [col for col in data.columns if col not in columnas_requeridas],
        "duplicate_row_count" : data.duplicated().sum(),
        "duplicate_supplier_id_row_count" : data.duplicated(subset=['supplier_id'],keep=False).sum(),
        "missing_value_count_by_column" : data.replace("N/A", np.nan).isnull().sum().to_dict(),
        "invalid_email_count" : data[data['contact_email'].str.contains('@') == False].shape[0],
        "invalid_unit_count" : data[data["units"].notna()][(data["units"] % 1 != 0)].shape[0],
        "country_values" : sorted(data["country"].unique())
        
    }

    def to_native(o):
      if isinstance(o, np.generic):
          return o.item()
      if isinstance(o, np.ndarray):
          return o.tolist()
      raise TypeError(f"{type(o).__name__} no es serializable")

    with open("submission/data_quality_report.json", "w", encoding="utf-8") as f:
      json.dump(result, f, ensure_ascii=False, indent=2, default=to_native)


    return result

    #raise NotImplementedError
