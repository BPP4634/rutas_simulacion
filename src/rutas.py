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