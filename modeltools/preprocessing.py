"""
Este módulo contiene helpers para el preprocesamiento de datos
La idea es tener herramientas que no estén en sklearn a disposición de la empresa
"""
import numpy as np

'''
Devuelve todas las columnas numéricas de un DataFrame
Entrada DataFrame
Salida Lista con las columnas numéricas del DataFrame de entrada
'''
def get_numerical_features(df):
    """ get_numerical features devuelve una lista con el nombre de las columnas que contienen datos de tipo numérico
    
    Parámetros
    ----------

    df: dataframe

    Ejemplos
    --------

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a":[1]})
    >>> get_numerical_features(df)
    ['a']

    """
    return list(df.select_dtypes(include=[np.number]).columns)
    