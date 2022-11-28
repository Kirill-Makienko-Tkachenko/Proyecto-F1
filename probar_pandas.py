#no hacerle caso a esto
import math
import pandas as pd

df = pd.read_csv(r"coordenadas_autodromo.csv",header=None)
df['Siguiente'] = df.shift(-1)

df.head(10)

#for i ,row in df.iterrows():
 #   print(i, row[0])
