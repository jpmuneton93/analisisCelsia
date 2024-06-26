from generators.generadorConsumo import generarDatos

import pandas as pd

def analizarDatos():
    datos=generarDatos()
    tabla=pd.DataFrame(datos, columns=['id', 'referencia', 'marca', 'capacidad', 'ciudad', 'responsable']) #se crea una tabla con pandas
    tabla.to_csv('archivo.csv',index=False) #para que solo salgan las columnas con los datos y no traiga nada adicional

analizarDatos()