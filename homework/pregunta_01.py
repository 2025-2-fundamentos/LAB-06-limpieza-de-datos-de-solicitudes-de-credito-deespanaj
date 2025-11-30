"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    """
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import numpy as np
import os





def pregunta_01():
   
    path = 'files/input/solicitudes_de_credito.csv'
    df = pd.read_csv(path, sep = ';')

    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df[['día', 'mes', 'año']] = df['fecha_de_beneficio'].str.split('/', expand=True)
    df.loc[df['año'].str.len() < 4, ['día', 'año']] = df.loc[df['año'].str.len() < 4, ['año', 'día']].values
    df['fecha_de_beneficio'] = df['año'] + '-' + df['mes'] + '-' + df['día']
    df.drop(['día', 'mes', 'año'], axis=1, inplace=True)

    object_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito']
    df[object_columns] = df[object_columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip())
    df['barrio'] = df['barrio'].str.lower().replace(['-', '_'], ' ', regex=True)

    df['monto_del_credito'] = df['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip()
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce')
    df['monto_del_credito'] = df['monto_del_credito'].fillna(0).astype(int)
    df['monto_del_credito'] = df['monto_del_credito'].astype(str).str.replace('.00', '')

    df.drop_duplicates(inplace=True)

    output_dir = 'files/output'
    os.makedirs(output_dir, exist_ok=True)

    output_path = f'{output_dir}/solicitudes_de_credito.csv'
    df.to_csv(output_path, sep=';', index=False)

    return df.head()