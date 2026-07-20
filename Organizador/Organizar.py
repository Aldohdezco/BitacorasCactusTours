from pathlib import Path
import re

# ==========================
# CONFIGURACIÓN
# ==========================
MES = 7
ANIO = 2026

ARCHIVO_ENTRADA = "bitacoras.md"
CARPETA_SALIDA = "salida"

# ==========================

Path(CARPETA_SALIDA).mkdir(exist_ok=True)

with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as f:
    lineas = f.readlines()

contenido_actual = []
dia_actual = None

patron = re.compile(r"^#\s+(\d+)\s*$")

def guardar_archivo(dia, contenido):
    if dia is None:
        return

    nombre = f"Bitácora {dia:02d}-{MES:02d}-{ANIO}.md"
    ruta = Path(CARPETA_SALIDA) / nombre

    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(contenido)

    print(f"Generado: {ruta}")

for linea in lineas:
    m = patron.match(linea)

    if m:
        # Guardar el archivo anterior
        guardar_archivo(dia_actual, contenido_actual)

        # Nuevo archivo
        dia_actual = int(m.group(1))
        contenido_actual = [
            f"# Bitácora {dia_actual:02d}/{MES:02d}/{ANIO}\n\n"
        ]
    else:
        if dia_actual is not None:
            contenido_actual.append(linea)

# Guardar el último archivo
guardar_archivo(dia_actual, contenido_actual)

print("Proceso terminado.")