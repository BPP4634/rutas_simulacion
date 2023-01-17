from parsear import *
from collections import namedtuple,Counter,defaultdict
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
    result={}
    for a in aux:
        result[a]=calcular_diferencia_km(aux[a])
    return result
