from rutas import *

def test_lee_rutas(rutas):
    print('Registros leídos:',len(rutas))
    print('Los tres primeros son:',rutas[:3])
    print('Los tres últimos son:',rutas[-3:])

def main():
    DATOS=lee_rutas('./data/rutas_motos.csv')
    test_lee_rutas(DATOS)

if __name__=='__main__':
    main()