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

def main():
    DATOS=lee_rutas('./data/rutas_motos.csv')
    # test_lee_rutas(DATOS)
    # test_acumular_kms_por_meses(DATOS)
    test_diferencias_kms_meses_anyo(DATOS)

if __name__=='__main__':
    main()