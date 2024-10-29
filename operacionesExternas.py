'''''
Para evitar problemas de recursividad en la importación de ciertos módulos
voy a poner en este módulo las funciones para que sean accedidas por otros módulos
'''''

'''''
Función para ser consumida por el resto de los módulos
Indicandole el tipo de operación (False para Recibos o True para Facturas)
Obtenemos todos los movimientos de un cliente
'''''
def obtenerOperacionesPorCliente(buscarCliente, buscarOperacion = False):
    # Inicializamos una lista vacía para almacenar las operaciones que encontremos
    listaOperaciones = []

    '''''
    Nombre del archivo: operaciones.csv
    Entramos al archivo EN MODO LECTURA
    '''''
    try:
        archivoOperaciones = open(r"operaciones.csv", "rt")
    except IOError:
        print("ERROR al abrir el archivo de operaciones")
    else:
        try:
            # Leemos el archivo
            linea = archivoOperaciones.readline()
            
            while linea:
                cliente, vendedor, operacion, monto = linea.split(";")

                '''''
                Si el cliente de la línea actual coincide con el cliente a buscar
                Y al mismo tiempo la operación de la línea actual coincide con la operación a buscar
                Entoncés ejecutamos el código dentro del if
                '''''
                if (int(cliente) == buscarCliente and bool(int(operacion)) == buscarOperacion):
                    listaOperaciones.append([int(cliente), int(vendedor), bool(int(operacion)), int(monto)])

                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:            
            archivoOperaciones.close()

    # Devolvemos la lista vacía o con los elementos encontrados
    return listaOperaciones