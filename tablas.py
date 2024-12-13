def crearTabla(columnas, filas, t_col = 36):
    # Imprimimos el primer renglón de "---" de la tabla
    print("-" * (t_col * len(columnas)))

    # Recorremos el nombre de las columnas
    fila_columnas = ""
    for i in range(len(columnas)):
        fila_columnas = fila_columnas + ("|" + columnas[i].center(t_col - 2) + "|")

    # Imprimimos los nombres de las columnas
    print(fila_columnas)

    # Cerramos el "---" de la tabla donde están los nombres de las columnas
    print("-" * (t_col * len(columnas)))

    # Creamos las filas con los datos
    if (len(filas) > 0):
        for i in range(len(filas)):
            contenido_fila = ""
            # Recorremos cada columna i de la fila k
            for k in range(len(columnas)):
                contenido_fila = contenido_fila + ("|" + str(filas[i][k]).center(t_col - 2) + "|")

            # Imprimimos el contenido de la fila y un separador
            print(contenido_fila)
            print("-" * (t_col * len(columnas)))
    else:
        # No hay registros
        # Así que mostramos un mensaje alertando esto
        print("|" + "No hay registros para mostrar".center((t_col * len(columnas)) - 2) + "|")
        print("-" * (t_col * len(columnas)))