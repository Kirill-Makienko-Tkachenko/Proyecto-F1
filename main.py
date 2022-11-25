# Simulacion Formula 1
# 25/11/2022
# Kirill Makienko Tkachenko
# Dulce Nahomi Bucio Rivas
# Desireé Espinosa Contreras
# Samuel Eric Miranda Álvarez
# Oscar Omar Cepeda Vázquez 

import math
import csv


# como nadien de ustedes estaban, dulce y kirill tomamos la desicion ejecutiva de trabajar con python default, sin pandas

# Importar .csv de excel
with open(r"coordenadas_autodromo.csv",'r') as file:
        reader= csv.reader(file)
        x = 0
        y = 0
        for row in reader:
            
            #row[0]     row[1]      row[2]              row[3]              row[4]
    #   Coordenada X  Coordenada Y  Tipo de segmento    Velocidad maxima    Helper_id
            #print(row[0], "\t" , row[1], "\t" , row[2], "\t" , row[3], "\t" , row[4])
            distanciaX = x - float(row[0])
            distanciaY = y - float(row[1])
            x = float(row[0])
            y = float(row[1])
            print("Distancia en X de estos 2 puntos: ", distanciaX, "Distancia en Y de estos 2 puntos: ", distanciaY)