"""
Este módulo contiene helpers para el preprocesamiento de datos
La idea es tener herramientas que no estén en sklearn a disposición de la empresa
"""
import numpy as np

"""
Devuelve todas las columnas numéricas de un DataFrame
Entrada DataFrame
Salida Lista con las columnas numéricas del DataFrame de entrada
"""


def get_numerical_features(df):
    """get_numerical features devuelve una lista con el nombre de las columnas que contienen datos de tipo numérico

    Parámetros
    ----------

    :param df: dataframe
    :type df: pandas.DataFrame
    :return: Lista con el nombre de las columnas con valores numéricos
    :rtype: List[str]

    Ejemplos
    --------

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a":[1]})
    >>> get_numerical_features(df)
    ['a']

    """

    return list(df.select_dtypes(include=[np.number]).columns)


"""
Función que suma cualquier número de valores numéricos
Entrada números
Salida La suma de todos los números recibidos ajusando el tipo
"""


def suma_n(*numeros):
    """
    Esta función suma n números

    Parámetros
    ----------

    :param *numeros: operandos
    :type *numeros: int, float, complex

    :raises: si los números no se pueden sumar

    :return: suma de todos los números
    :rtype: int, float, complex

    Ejemplos
    --------

    >>> from modeltools.preprocessing import suma_n
    >>> suma_n(5,5,5,5,5,5,5,5,5, 23.12, complex(3,4))
    (71.12+4j)

    """

    suma = 0

    for numero in numeros:
        suma = suma + numero

    return suma


"""_summary_
Función para probar el autodocstring
Se crea la documentación para las variables
"""


def hola(a, b, c, d):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
        c (_type_): _description_
        d (_type_): _description_
    """

    return 1
