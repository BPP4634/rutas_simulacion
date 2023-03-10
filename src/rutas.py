from parsear import *
from collections import namedtuple,defaultdict
import csv

Ruta=namedtuple('Ruta','ciudad_inicio,coordenada,fecha_ruta,km,gasolineras,dificultad,zona_descanso,vel_max,vel_min')

def lee_rutas(fichero):
    result=[]
    with open(fichero,encoding='UTF-8') as f:
        lector=csv.reader(f,delimiter=';')
        next(lector)
        for ciudad_inicio,coordenada,fecha_ruta,km,gasolineras,dificultad,zona_descanso,vel_max,vel_min in lector:
            ciudad_inicio=ciudad_inicio.strip()
            coordenada=parsear_coordenada(coordenada)
            fecha_ruta=parsear_fecha(fecha_ruta)
            km=float(km.strip())
            gasolineras=int(gasolineras.strip())
            dificultad=dificultad.strip()
            zona_descanso=parsear_booleano(zona_descanso)
            vel_max=int(vel_max.strip())
            vel_min=int(vel_min.strip())
            result.append(Ruta(ciudad_inicio,coordenada,fecha_ruta,km,gasolineras,dificultad,zona_descanso,vel_max,vel_min))
    return result

def acumular_kms_por_meses(rutas):
    result=defaultdict(lambda:[0.0]*12)
    for r in rutas:
        result[r.fecha_ruta.year][r.fecha_ruta.month-1]+=r.km
    return dict(sorted(result.items()))

def calcular_diferencia_km(kms):
    return [e2-e1 for e1,e2 in zip(kms,kms[1:])]

def diferencias_kms_meses_anyo(rutas):
    aux=acumular_kms_por_meses(rutas)
    return {a:calcular_diferencia_km(aux[a]) for a in aux}

def distancia_Manhattan(coor1,coor2):
    return abs(coor1.latitud-coor2.latitud)+abs(coor1.longitud-coor2.longitud)

def top_rutas_lejanas(rutas,n,c,km_min=None):
    result=rutas
    if km_min!=None:
        result=[r for r in rutas if r.km>km_min]
    return sorted(result,key=lambda x:distancia_Manhattan(c,x.coordenada),reverse=True)[:n]

def ciudades_top_tiempo_dificultad(rutas,n=3):
    result=defaultdict(list)
    for r in rutas:
        if r.zona_descanso:
            result[r.dificultad]+=[r]
    for r in result:
        result[r]=[s.ciudad_inicio for s in sorted(result[r],key=lambda x:(x.km/x.vel_min),reverse=True)[:n]]
    return result