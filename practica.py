#consume los datos del archivo suelo.csv
#almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
#gráfico de dispersión de los totales de superficie por TIPUSSOL
#gráfico de barras de la superficie media de los 10 primeros NOM_ENS
#gráfico circular de la superfice de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt
def consumiInversiones():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','SUPERFICIE','TIPUSSOL','CODI_TIPUSSOL']]
    #print(df)
    df.CODI_TIPUSSOL.plot.hist()
    plt.show()
consumiInversiones()