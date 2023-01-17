from rutas import *

def test_lee_rutas(rutas):
    print('Registros leídos:',len(rutas))
    print('Los tres primeros son:',rutas[:3])
    print('Los tres últimos son:',rutas[-3:])

def test_acumular_kms_por_meses(rutas):
    akpm=acumular_kms_por_meses(rutas)
    print('Los kms recorridos por mes en cada año son:')
    for a in akpm:
        print(f'En {a}: {akpm[a]}')

def test_diferencias_kms_meses_anyo(rutas):
    dkma=diferencias_kms_meses_anyo(rutas)
    print('Las diferencias de kms recorridos entre los meses de cada año son:')
    for d in dkma:
        print(f'En {d}: {dkma[d]}')

def test_top_rutas_lejanas(rutas,n,c,km_min=None):
    trl=top_rutas_lejanas(rutas,n,c,km_min)
    if km_min==None:
        print(f'Las {n} rutas más lejanas a la coordenada {c.latitud,c.longitud} son:')
    else:
        print(f'Las {n} rutas más lejanas a la coordenada {c.latitud,c.longitud} con más de {km_min} km son:')
    print(trl)

def test_ciudades_top_tiempo_dificultad(rutas,n=3):
    cttd=ciudades_top_tiempo_dificultad(rutas,n)
    print(f'Las {n} ciudades con zona de descanso que más tiempo han tardado en hacerse son:')
    for c in cttd:
        print(f'En dificultad {c}: {cttd[c]}')

def main():
    DATOS=lee_rutas('./data/rutas_motos.csv')
    # test_lee_rutas(DATOS)
    # test_acumular_kms_por_meses(DATOS)
    # test_diferencias_kms_meses_anyo(DATOS)
    # test_top_rutas_lejanas(DATOS,2,Coordenada(35.15,-8.76))
    # test_top_rutas_lejanas(DATOS,2,Coordenada(35.15,-8.76),100)
    test_ciudades_top_tiempo_dificultad(DATOS)

if __name__=='__main__':
    main()