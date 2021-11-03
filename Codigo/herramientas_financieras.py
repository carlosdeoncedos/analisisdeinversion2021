import pandas as pd
import numpy as np

def funcion_sumar(valor_1, valor_2):
    suma = valor_1 + valor_2
    print(suma)
    
    return suma


def importar_bloomberg(accion):
    
    url = f'http://bit.ly/oncedos-{accion}'
    
    columnas_a_importar = ['Date', 'PX_OPEN', 'PX_HIGH', 'PX_LOW', 'PX_LAST']
    
    df = pd.read_csv(url, skiprows = 6, index_col = 0, parse_dates = True, dayfirst = True, 
                 usecols = columnas_a_importar)
    
    df.rename({'PX_LAST':'Cierre', 'PX_OPEN':'Apertura', 'PX_HIGH':'Maximo', 'PX_LOW':'Minimo'}, axis = 1,
          inplace = True)
    
    orden_columnas = ['Apertura', 'Maximo', 'Minimo', 'Cierre']
    
    df = df.reindex(columns=orden_columnas)
    df.sort_index(inplace = True)
    
    return df


