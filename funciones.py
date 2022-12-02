# Simulacion Formula 1
# 25/11/2022
# Kirill Makienko Tkachenko
#Dulce Nahomi Bucio Rivas
# Agreguen sus nombres si abren este archivo


import math
velMaxC = 320 # Km/H
pesoC = 798 # Kg
aceleracionC = 35.71 # 100 Km/H en 2.8 segundos, por lo tanto esta en m/s
#frenadoC = int(input()) # Vamos a sacarlo con mi coche
friccionC = 0.8 # Coeficiente de friccion de las llantas con el piso
resistenciaC = 1.1 # CX
densidadA = 1.225


def aceleracion(v1,v2,v3,v4,v5):
    x = (v1+v2+v3+v4+v5)/5
    return x

def distanciaSiguienteSegmento(x0,x1,y0,y1):
    resultado = math.sqrt(((x1-x0)**2)+((y1-y0)**2))
    resultado = round(resultado,3)
    return resultado

def potencia(vel):
    potenciaA = 1/2*densidadA*resistenciaC*friccionC*vel*vel
    return potenciaA

def resistenciaAerodinamica(vel):
    resistencia = 1/2*densidadA*resistenciaC*friccionC*vel*vel*vel
    return resistencia