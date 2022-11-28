# Simulacion Formula 1
# 25/11/2022
# Kirill Makienko Tkachenko
# Agreguen sus nombres si abren este archivo



import math


def aceleracion(v1,v2,v3,v4,v5):
    x = (v1+v2+v3+v4+v5)/5
    return x

def distanciaSiguienteSegmento(x0,x1,y0,y1):
    resultado = math.sqrt(((x1-x0)**2)+((y1-y0)**2))
    return resultado