import datetime
from random import randint

# Comprobar si un archivo existe
def comprobarArchivo(nombreArchivo):
    try:
        archivo = open(r""+nombreArchivo, "rt")
    except IOError:
        existeArchivo = False
    else:
        # El archivo existe
        existeArchivo = True

        archivo.close()

    return existeArchivo

# Generar archivo de reporte
def generarReporte(datos = [], nombreReporte = "reporte"):
    while True:
        # Generamos le nombre del archivo
        now = datetime.datetime.now()
        archivoID = now.strftime("%Y_%m_%d-%H-%M-%S")
        nombreArchivo = f"reportes/{nombreReporte}_{archivoID}.csv"
        
        # Si el archivo no existe rompemos el ciclo
        if(comprobarArchivo(nombreArchivo) == False):
            break;
    
    try:
        archivoReportes = open(r""+nombreArchivo, "wt")
    except IOError:
        print("ERROR al abrir el archivo de reportes")
    else:
        for i in range(len(datos)):
            archivoReportes.write(datos[i])
            archivoReportes.write("\n")

        archivoReportes.close()