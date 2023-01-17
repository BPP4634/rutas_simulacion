from collections import namedtuple
from datetime import datetime

Coordenada=namedtuple('Coordenada','latitud,longitud')

def parsear_coordenada(cad):
    latitud,longitud=cad.split('/')
    return Coordenada(float(latitud.strip()),float(longitud.strip()))

def parsear_fecha(fecha):
    if fecha=='':
        result=datetime.today().date()
    else:
        result=datetime.strptime(fecha.strip(),'%m/%d/%Y').date()
    return result

def parsear_booleano(cad):
    return cad.strip().upper()=='TRUE'