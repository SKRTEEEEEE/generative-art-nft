import os

# Ruta de la carpeta que contiene los archivos que deseas renombrar
ruta_carpeta = 'C:/Users/Adan/Pictures/houseLuxury/houseLuxuryWhite1meta/json'

# Cambia al directorio de la carpeta
os.chdir(ruta_carpeta)

# Lista todos los archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Ordena los archivos alfabéticamente (esto asegura que sigan un orden específico)
archivos.sort()

# Itera sobre cada archivo y renómbralo
for archivo in archivos:
    # Obtén el nombre del archivo sin la extensión
    nombre_sin_extension = os.path.splitext(archivo)[0]
    
    # Renombra el archivo eliminando solo la extensión
    os.rename(archivo, nombre_sin_extension)
