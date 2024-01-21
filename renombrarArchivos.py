import os

# Ruta de la carpeta que contiene los archivos que deseas renombrar
ruta_carpeta = 'C:/Users/Adan/Pictures/houseLuxury/houseLuxuryWhite1'

# Cambia al directorio de la carpeta
os.chdir(ruta_carpeta)

# Lista todos los archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Ordena los archivos alfabéticamente (esto asegura que sigan un orden específico)
archivos.sort()

# Inicializa un contador para la numeración
contador = 1

# Itera sobre cada archivo y renómbralo
for archivo in archivos:
    # Construye el nuevo nombre del archivo usando el contador
    nuevo_nombre = str(contador) + os.path.splitext(archivo)[1]
    
    # Renombra el archivo
    os.rename(archivo, nuevo_nombre)
    
    # Incrementa el contador para el próximo archivo
    contador += 1
