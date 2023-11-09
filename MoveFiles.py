import os
import shutil

# Ruta de la carpeta de origen
ruta_origen = "C:\\Users\\alan.riquelmes\\Desktop\\PRUEBA"

# Ruta de la carpeta de destino
ruta_destino = "C:\\Users\\alan.riquelmes\\Desktop\\FCA"

# Utilizamos la función os.listdir para obtener una lista de archivos en la carpeta de origen
archivos = os.listdir(ruta_origen)

# Iteramos sobre la lista de archivos y utilizamos la función os.rename para mover cada archivo a la carpeta de destino
for archivo in archivos:
    ruta_archivo_origen = os.path.join(ruta_origen, archivo)
    ruta_archivo_destino = os.path.join(ruta_destino, archivo)

    # Comprobamos si el archivo ya existe en la carpeta de destino
    num = 1
    while os.path.exists(ruta_archivo_destino):
        # Si el archivo ya existe, agregamos un sufijo numérico al nombre del archivo y lo comprobamos nuevamente
        nombre, extension = os.path.splitext(archivo)
        nuevo_nombre = f"{nombre} ({num}){extension}"
        ruta_archivo_destino = os.path.join(ruta_destino, nuevo_nombre)
        num += 1
        # Imprimimos el nombre de archivo que se está comprobando en cada iteración
        print(f"Comprobando {ruta_archivo_destino}")
        # Si encontramos un nombre de archivo que no existe en la carpeta de destino después de 100 iteraciones, salimos del bucle while
        if not os.path.exists(ruta_archivo_destino) and num <= 100:
            break

    # Movemos el archivo a la carpeta de destino
    os.rename(ruta_archivo_origen, ruta_archivo_destino)



