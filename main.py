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

velMaxC = 320 # Km/H
pesoC = 798 # Kg
aceleracionC = 35.71 # 100 Km/H en 2.8 segundos, por lo tanto esta en m/s
#frenadoC = int(input()) # Vamos a sacarlo con mi coche
friccionC = 0.8 # Coeficiente de friccion de las llantas con el piso
resistenciaC = 1.1 # CX


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






# Por hacer en esta seccion
# hacer que sirva con caso 0 0 1 0, tal vez meter esta cosa en algun array o algos


i = 0
p = 3
vel = 0 # Velocidad inicial del coche = 0, parte del reposo
while i < 332:
# Vamos a hacer logica de segmentos rectos
        if int(tipoCurva[i]) == 0:
                
                input()
                if int(tipoCurva[i+p]) or int(tipoCurva[i+p-1]) == 1:
                        disTot = distanciaSiguienteSegmento(arrX[i],arrX[i+p],arrY[i],arrY[i+p])
                        print("Distancia total hasta siguiente segmento curvo: " , disTot)
#                        distancia disponible > distancia para frenar:
                        p -= 1
                        
                
        if int(tipoCurva[i]) == 1:
                print(tipoCurva[i], tipoCurva[i+1],tipoCurva[i+2],tipoCurva[i+p])
                input()
                if int(tipoCurva[i+p]) == 0:
                        disTot = distanciaSiguienteSegmento(arrX[i],arrX[i+p],arrY[i],arrY[i+p])
                        print("Distancia total hasta siguiente segmento recto: " , disTot)
#                        distancia disponible > distancia para frenar:
                        p -= 1
                
                #acelerar
        if p == 0:
                p = 3
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

