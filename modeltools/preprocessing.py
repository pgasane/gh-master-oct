"""
Este módulo contiene helpers para el preprocesamiento de datos
La idea es tener herramientas que no estén en sklearn a disposición de la empresa
"""
import numpy as np

# Devuelve todas las columnas numéricas de un DataFrame.
# Entrada DataFrame.
# Salida Lista con las columnas numéricas del DataFrame de entrada.


def get_numerical_features(data_frame):
    """get_numerical features devuelve una lista con el nombre de las columnas
     que contienen datos de tipo numérico

    Parámetros
    ----------

    :param data_frame: dataframe
    :type data_frame: pandas.DataFrame
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

    return list(data_frame.select_dtypes(include=[np.number]).columns)


# Función que suma cualquier número de valores numéricos.
# Entrada números.
# Salida La suma de todos los números recibidos ajusando el tipo."""


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


# This is a docstring which describes the module.


def hola(a_b, b_c, c_d, d_e):
    """_summary_

    Args:
        a_b (_type_): _description_
        b_c (_type_): _description_
        c_d (_type_): _description_
        d_e (_type_): _description_

    Returns:
        _type_: _description_
    """
    # This is comment which describes a particular part of the module.
    a_b = 1
    b_c = 2
    c_d = 3
    d_e = 4

    return a_b, b_c, c_d, d_e
