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
    return list(df.select_dtypes(include=[np.number]).columns)