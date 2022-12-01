# Simulacion Formula 1
# 25/11/2022
# Kirill Makienko Tkachenko
# Dulce Nahomi Bucio Rivas
# Desireé Espinosa Contreras
# Samuel Eric Miranda Álvarez
# Oscar Omar Cepeda Vázquez 

import math
import csv
from funciones import *
import sys, time
import plotly.graph_objects as go
import matplotlib as plt
import numpy as np

# como nadien de ustedes estaban, dulce y kirill tomamos la desicion ejecutiva de trabajar con python default, sin pandas




# Vamos a transformar los datos de Rows que es dificil de iterar a travez y vamos a convertirlo en un array donde es mas simple iterar
#sabemos que nuestra catidad de datos es de 332, por lo que para poder saber 10 puntos adeltante que tipo de segmento es, vamos a tener que añadir 10 valores "0" en x,y y 10 valores 2 en tipoCurva para indicarle al programa que ya va a terminar la simulacion
arrX = []
arrY = []
velTotales = []



velMaxC = 300 # Km/H
pesoC = 798 # Kg
aceleracionC = 35.71 # 100 Km/H en 2.8 segundos, por lo tanto esta en m/s
frenadoC = 10 # Calculado a partir de mi poderosisismo Yaris
friccionC = 0.8 # Coeficiente de friccion de las llantas con el piso
resistenciaC = 1.1 # CX
densidadA = 1.225


# Importar .csv de excel y escribir sus datos en un array de python
with open(r"coordenadas_velocidades.csv",'r') as file:
        reader= csv.reader(file)
        for row in reader:
            arrX.append(float(row[0]))
            arrY.append(float(row[1]))
            velTotales.append(float(row[2]))
            #row[0]     row[1]      row[2]              
    #   Coordenada X  Coordenada Y  VElocidad en cada punto    
    #                         Tipo de segmento: 0 - recta, 1 - curva
            #print(row[0], "\t" , row[1], "\t" , row[2])
file.close()

#print(arrX)
#print(arrY)
print(velTotales)
i = 0
#while i < 332: