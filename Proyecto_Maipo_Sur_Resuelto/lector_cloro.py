"""Simulación didáctica. No contiene comunicación con PLC ni red."""
import os


def leer_cloro_simulado():
    if not os.environ.get("PLC_PASSWORD"):
        raise RuntimeError("Falta la variable de entorno PLC_PASSWORD")
    return {"planta": "Maipo Sur - laboratorio", "cloro_mg_l": 0.7}


if __name__ == "__main__":
    print(f"Lectura simulada: {leer_cloro_simulado()['cloro_mg_l']} mg/L")
