"""Servicio exclusivamente simulado: no se conecta con PLC ni redes."""
import os


def leer_cloro_simulado():
    if not os.getenv('PLC_PASSWORD'):
        raise RuntimeError('Falta la variable PLC_PASSWORD')
    return {'planta': 'Maipo Sur - laboratorio', 'cloro_mg_l': 0.7}


if __name__ == '__main__':
    print('Lectura simulada: %.1f mg/L' % leer_cloro_simulado()['cloro_mg_l'])
