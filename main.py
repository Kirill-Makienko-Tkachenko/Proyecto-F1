# Simulacion Formula 1
# 25/11/2022
# Kirill Makienko Tkachenko
# Dulce Nahomi Bucio Rivas
# Desireé Espinosa Contreras
# Samuel Eric Miranda Álvarez
# Oscar Omar Cepeda Vázquez 

import math
import csv
import pandas as pd
from funciones import *
df = pd.read_csv(r"coordenadas_autodromo.csv",header=None)

# como nadien de ustedes estaban, dulce y kirill tomamos la desicion ejecutiva de trabajar con python default, sin pandas

# Por hacer:
# Logica de curvas y rectas
# añadir 5 "0" a todos los arrays 




# Vamos a transformar los datos de Rows que es dificil de iterar a travez y vamos a convertirlo en un array donde es mas simple iterar
#sabemos que nuestra catidad de datos es de 332, por lo que para poder saber 10 puntos adeltante que tipo de segmento es, vamos a tener que añadir 10 valores "0" en x,y y 10 valores 2 en tipoCurva para indicarle al programa que ya va a terminar la simulacion
arrX = []
arrY = []
tipoCurva = []
velMax = []
arrAyuda = [0,0,0,0,0] #Añadir 5 ceros para poder hacer i+1,i+2,i+3,i+4
arrCur = [2,2,2,2,2] #Añadir 5 Dos para poder hacer i+1,i+2,i+3,i+4


# Importar .csv de excel y escribir sus datos en un array de python
with open(r"coordenadas_autodromo.csv",'r') as file:
        reader= csv.reader(file)
        for row in reader:
            arrX.append(float(row[0]))
            arrY.append(float(row[1]))
            tipoCurva.append(float(row[2]))
            velMax.append(row[3])
            #row[0]     row[1]      row[2]              row[3]              row[4]
    #   Coordenada X  Coordenada Y  Tipo de segmento    Velocidad maxima    Helper_id
    #                         Tipo de segmento: 0 - recta, 1 - curva
            #print(row[0], "\t" , row[1], "\t" , row[2], "\t" , row[3], "\t" , row[4])


arrX.append(arrAyuda)
arrY.append(arrAyuda)
velMax.append(arrAyuda)
tipoCurva.append(arrCur)


i = 0

while i < 332:
        print(arrX[i],arrX[i+1],arrX[i+2],arrX[i+3],arrX[i+4])
        v1 = arrX[i]
        v2 = arrX[i+1]
        v3 = arrX[i+2]
        v4=  arrX[i+3]
        v5=  arrX[i+4]
        vf = aceleracion(v1,v2,v3,v4,v5)
        print(vf)
        i += 1






#logica que tal vez podamos usar en el futuro

#            if float(row[2]) == 0:    
 #               distanciaX = x - float(row[0])
  #              distanciaY = y - float(row[1])
   #             x = float(row[0])
    #            y = float(row[1])
     #           if 1 in row[]
#
 #               print("Distancia en X de estos 2 puntos: ", distanciaX, "Distancia en Y de estos 2 puntos: ", distanciaY)
  #          i += 1

