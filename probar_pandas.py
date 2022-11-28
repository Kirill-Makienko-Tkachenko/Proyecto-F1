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

#velMaxC = int(input()) # Velocidad Maxima coche
#pesoC = int(input()) # Peso del coche
#aceleracionC = int(input()) # Aceleracion del coche
#frenadoC = int(input()) # Capacidad de frenado del coche
#friccionC = int(input()) # Coeficiente de friccion de las llantas con el piso
#resistenciaC = int(input()) # Resistencia del aire con respecto al coche


# Importar .csv de excel y escribir sus datos en un array de python
with open(r"coordenadas_autodromo.csv",'r') as file:
        reader= csv.reader(file)
        for row in reader:
            arrX.append(float(row[0]))
            arrY.append(float(row[1]))
            tipoCurva.append(int(row[2]))
            velMax.append(row[3])
            #row[0]     row[1]      row[2]              row[3]              row[4]
    #   Coordenada X  Coordenada Y  Tipo de segmento    Velocidad maxima    Helper_id
    #                         Tipo de segmento: 0 - recta, 1 - curva
            #print(row[0], "\t" , row[1], "\t" , row[2], "\t" , row[3], "\t" , row[4])
file.close()

i = 0
while i < 5: # Este Append es para decirle al programa que si puede ir a "i" + de 332 para saber la distancia que falta para el siguiente tipo de segmento
        arrX.append(0)
        arrY.append(0)
        velMax.append(0)
        tipoCurva.append(0)
        i += 1


i = 0
p = 4
vel = 0 # Velocidad inicial del coche = 0, parte del reposo
while i < 332:
# Vamos a hacer logica de segmentos rectos
        if int(tipoCurva[i]) == 0:
                print(tipoCurva[i], tipoCurva[i+p])
                input()
                if int(tipoCurva[i+p]) == 1:
                        disTot = distanciaSiguienteSegmento(arrX[i],arrX[i+p],arrY[i],arrY[i+p])
                        print("Distancia total hasta siguiente segmento" , disTot)
#                        distancia disponible > distancia para frenar:
                        p -= 1
                
        if int(row[2]) == 1:
                print("No pasa nada xd")
                
                #acelerar
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
