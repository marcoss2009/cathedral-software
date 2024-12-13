from terminal import limpiarTerminal
from tablas import crearTabla
from clientes import verificarCliente, cantidadClientes, obtenerClientes, actualizarSaldo
from vendedores import verificarVendedor, obtenerVendedores
from random import randint
from reportes import generarReporte

def cargarOpereacion(cliente, vendedor, operacion, monto):
    '''''
    Nombre del archivo: operaciones.csv
    Si el archivo no existe vamos a tener que crearlo, muy posiblemente esta condición se presente en la primera ejecución
    '''''
    try:
        archivoOperaciones = open(r"operaciones.csv", "at") # Se podía usar append?
    except IOError:
        print("ERROR al abrir el archivo de operaciones")
    else:
        archivoOperaciones.write(str(cliente) + ";" + str(vendedor) + ";" + str(operacion) + ";" + str(monto) + "\n")

        # Actualizamos el saldo del cliente
        actualizarSaldo(cliente, monto, operacion)
        archivoOperaciones.close()

def leerOperaciones(busqueda = "operacion", filtro = 0):
    filas = []
    datosReporte = []

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
                if (
                    (busqueda == "operacion" and int(operacion) == filtro)
                    or (busqueda == "cliente" and int(cliente) == filtro)
                    or (busqueda == "vendedor" and int(vendedor) == filtro)
                ):
                    # Lo mostramos en Modo Tabla
                    # Al monto primero lo convertimos a int para eliminar el salto de línea
                    # y luego a texto nuevamente para poder concatenarlo con el símbolo "$"
                    filas.append([cliente, vendedor, ("Factura" if bool(int(operacion)) == True else "Recibo"), "$" + str(int(monto))])

                    datosReporte.append(cliente + ";" + vendedor + ";" + operacion + ";" + str(int(monto))) # Le borramos el salto de línea a monto
                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:        
            archivoOperaciones.close()

    # Generamos el archivo de reporte
    if busqueda == "operacion":
        nombreArchivo = "operaciones_facturas" if bool(filtro) == True else "operaciones_recibos"
    elif busqueda == "cliente":
        nombreArchivo = "operaciones_cliente_" + str(filtro)
    elif busqueda == "vendedor":
        nombreArchivo = "operaciones_vendedor_" + str(filtro)

    # Generamos el archivo
    generarReporte(datosReporte, nombreArchivo)
    
    # Creamos la Tabla
    # Primero definimos el nombre de las columnas
    columnasOperaciones = ["Cliente", "Vendedor", "Tipo de Operación", "Monto"]
    crearTabla(columnasOperaciones, filas)

def cargaOperaciones():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Carga de Operaciones ".center(80,'-'))
    
    # Tenemos suficiente cantidad de clientes para comenzar a cargar operaciones?
    if (cantidadClientes() <= 0):
        print(" No hay suficiente cantidad de clientes para cargar una operación. ".center(80,'-'))
    else:
        '''''
        Solicitamos el Número de Cliente
        Creamos una excpción si el usuario ingresa algo distinto a un número
        Luego tendremos que verificar si este cliente existe con ayuda de alguna función del módulo de Clientes para tal fin

        Al igual que en el menú, cliente va a valer cero hasta que el cliente ingresado sea válido
        '''''
        while(True):
            try:
                cliente = int(input("Ingrese el Número de Cliente: "))
            except ValueError:
                print('ERROR: El Número de Cliente solo puede contener números')
            else:
                '''''
                Verificamos si el cliente existe
                Si el cliente no existe entoncés su valor vuelve a ser 0
                y volvemos a pedir el cliente infinitamente hasta que ingrese un cliente válido
                '''''
                if verificarCliente(cliente) == False:
                    print('ERROR: El Cliente ingresado no existe')
                else:
                    # El cliente existe, rompemos el ciclo y continuamos con la operación
                    break;

        '''''
        Solicitamos el Vendedor
        No necesitaremos una excepción debido a que el vendedor es un valor string
        Luego tendremos que verificar si este vendedor existe con ayuda de alguna función del módulo de Vendedores para tal fin

        Al igual que en el menú, vendedor va a valer cero hasta que el vendedor ingresado sea válido
        '''''
        vendedor = 0
        while(vendedor == 0):
            try:
                vendedor = int(input("Ingrese el Número de Vendedor: "))
            except ValueError:
                print('ERROR: El Número de Vendedor solo puede contener números')
            else:
                '''''
                Verificamos si el vendedor existe
                Si el vendedor no existe entoncés su valor vuelve a ser 0
                y volvemos a pedir el vendedor infinitamente hasta que ingrese un vendedor válido
                '''''
                if verificarVendedor(vendedor) == False:
                    print('ERROR: El Vendedor ingresado no existe')
                    vendedor = 0
            
        '''''
        Solicitamos el Tipo de Operación
        Creamos una excpción si el usuario ingresa algo distinto a un número
        Luego tendremos que verificar si el valor es 0 o 1
        '''''
        operacion = -1
        while (operacion == -1):
            try:
                operacion = int(input("Ingrese 0 si es Recibo o 1 si es Factura: "))
            except ValueError:
                print('ERROR: El Tipo de Operación debe ser un número')
            else:
                if operacion < 0 or operacion > 1:
                    print('ERROR: El Tipo de Operación debe ser 0 para Recibo o 1 para Factura')
                    operacion = -1

        '''''
        Solicitamos el Monto de Operación
        Creamos una excpción si el usuario ingresa algo distinto a un número
        Luego tendremos que verificar si el monto es mayor a cero
        '''''
        monto = 0
        while (monto == 0):
            try:
                monto  = int(input("Ingrese Monto de Operación: "))
            except ValueError:
                print('ERROR: El Monto de Operación debe ser un número')
            else:
                if (monto <= 0):
                    print('ERROR: El Monto de Operación debe ser mayor a cero')
                    monto = 0

        '''''
        La operación fue Cargada de Forma Exitosa
        Lo guardamos en el archivo y seguimos
        '''''
        cargarOpereacion(cliente, vendedor, operacion, monto)
        print(" Operación cargada exitosamente ".center(80,'-'))

    input("Presione Enter para continuar...")

def reporteFacturasRecibos():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Informe de Movimientos por Facturas y Recibos ".center(80,'-'))

    while (True):
        try:
            filtro = int(input("Ingrese 0 para Recibos o 1 para Facturas: "))
        except ValueError:
            print("ERROR: El valor debe ser 0 para Recibos o 1 para Facturas")
        else:
            if filtro < 0 or filtro > 1:
                print("ERROR: El valor ingresado es incorrecto.")
            else:
                # El filtro es correcto, rompemos el ciclo y continuamos
                break;

    # Ahora vamos a leer todos los registros que cumplan con esta condición
    leerOperaciones("operacion", filtro)

    # Leemos cualquier tecla para volver al menú principal
    input("Presione Enter para continuar...")

def reporteClienteVendedor():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Informe de Movimientos filtrados por Cliente y Vendedor ".center(80,'-'))
    
    # Hay suficiente cantidad de operaciones para mostrar estos datos?
    if (cantidadOperaciones() <= 0):
        print(" No hay suficiente cantidad de datos para ejecutar esta operación. ".center(80,'-'))
    else:
        while (True):
            try:
                filtro = int(input("Ingrese 0 para filtrar por Cliente o 1 para filtrar por Vendedor: "))
            except ValueError:
                print("ERROR: El valor debe ser 0 para Cliente o 1 para Vendedor")
            else:
                if filtro < 0 or filtro > 1:
                    print("ERROR: El valor ingresado es incorrecto.")
                else:
                    # El filtro es correcto, rompemos el ciclo y continuamos
                    break;

        '''''
        Wait a minute...
        Esto no termina acá lamentablamente...
        Ahora tenemos que verificar si el vendedor o cliente existe
        antes de empezar a filtrar los registros
        '''''
        while True:
            if (filtro == 0):
                # Filtramos por Cliente
                try:
                    valorBuscar = int(input("Ingrese el Código del Cliente para filtrar: "))
                except ValueError:
                    print('ERROR: El Número de Cliente solo puede contener números')
                else:
                    '''''
                    Verificamos si el cliente existe
                    Si el cliente no existe entoncés su valor vuelve a ser 0
                    y volvemos a pedir el cliente infinitamente hasta que ingrese un cliente válido
                    '''''
                    if verificarCliente(valorBuscar) == False:
                        print('ERROR: El Cliente ingresado no existe')
                    else:
                        # El cliente existe, rompemos el ciclo y continuamos
                        break;
            else:
                # Filtramos por Vendedor
                try:
                    valorBuscar = int(input("Ingrese el Código de Vendedor para filtrar: "))
                except ValueError:
                    print('ERROR: El Código de Vendedor solo puede contener números')
                else:
                    '''''
                    Verificamos si el vendedor existe
                    Si el vendedor no existe entoncés su valor vuelve a ser 0
                    y volvemos a pedir el vendedor infinitamente hasta que ingrese un vendedor válido
                    '''''
                    if verificarVendedor(valorBuscar) == False:
                        print('ERROR: El Vendedor ingresado no existe')
                    else:
                        # El vendedor existe, rompemos el ciclo y continuamos...
                        break;

        # Ahora vamos a leer todos los registros que cumplan con esta condición
        leerOperaciones("vendedor" if bool(filtro) == True else "cliente", valorBuscar)

    # Leemos cualquier tecla para volver al menú principal
    input("Presione Enter para continuar...")

def generarOperacionesRandom():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Generar Operaciones al Azar ".center(80,'-'))

    # Obtenemos la lista de clientes
    clientes = obtenerClientes()

    # Verificamos si tenemos la suficiente cantidad de clientes para generar operaciones al azar
    if len(clientes) <= 0:
        print(" No hay suficiente cantidad de datos para ejecutar esta operación. ".center(80,'-'))
    else:
        # Obtener un número entre 1 y 20 para generar x cantidad de operaciones
        cantidadOperaciones = randint(1, 20)

        # Perfecto, lo que necesitamos para generar una operación son los siguientes parámetros
        # Clientes, Vendedores, Tipo de Operacion y Monto
        # Lo repetimos la cantidad de veces que obtuvimos arriba
        
        # Obtenemos la lista de vendedores
        vendedores = obtenerVendedores()

        for i in range(cantidadOperaciones):
            # Tomamos el índice de un cliente al azar
            clienteRandom = randint(0,len(clientes) - 1)

            # Tomamos el índice de un vendedor al azar
            vendedorRandom = randint(0, len(vendedores) - 1)

            # Vamos a determinar si esto va a ser una factura o un recibo
            tipoOperacion = randint(0, 1)

            # Por último tomamos un monto random, preferentemente de 4 dígitos
            montoOperacion = randint(1000, 9999)

            # Perfecto, cargamos la operacion
            cargarOpereacion(clientes[clienteRandom], vendedores[vendedorRandom], tipoOperacion, montoOperacion)

        print(f" Se han generado {cantidadOperaciones} de operaciones al azar ".center(80, '-'))
        
    input("Presione Enter para continuar...")

def cuentaCorriente():
    # Limpiamos la terminal 
    limpiarTerminal()

    print(" Vista de Cuenta Corriente por Cliente ".center(80,'-'))

    # Hay suficiente cantidad de operaciones para mostrar estos datos?
    if (cantidadOperaciones() <= 0):
        print(" No hay suficiente cantidad de datos para ejecutar esta operación. ".center(80,'-'))
    else:
        # Vamos a solicitar un cliente
        while True:
            try:
                clienteBuscar = int(input("Ingrese el Número de Cliente para consultar: "))
            except ValueError:
                print("ERROR: El Número de Cliente debe ser un número")
            else:
                # Verificamos si el cliente existe
                if (verificarCliente(clienteBuscar) == False):
                    print("El cliente ingresado no existe.")
                else:
                    # El cliente existe, rompemos el ciclo y continuamos
                    break;

        # Seteamos la tabla
        columnasMovimientos = ["Movimiento", "Debe", "Haber"]
        filasMovimientos = []
        debe = 0
        haber = 0

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
                    if (int(cliente) == clienteBuscar):
                        # Lo mostramos en Modo Tabla
                        # Al monto primero lo convertimos a int para eliminar el salto de línea
                        # y luego a texto nuevamente para poder concatenarlo con el símbolo "$"
                        filasMovimientos.append([("Factura" if bool(int(operacion)) == True else "Recibo"), ("$" + str(int(monto)) if bool(int(operacion)) == True else ""), ("" if bool(int(operacion)) == True else "$" + str(int(monto)))])

                        # Sumamos Debe o Haber
                        if bool(int(operacion)) == True:
                            # Es una Factura, sumamos en Debe
                            debe = debe + int(monto)
                        else:
                            # Es un Recibo, sumamos en Haner
                            haber = haber + int(monto)

                    # Leemos la próxima línea
                    linea = archivoOperaciones.readline()
            finally:            
                archivoOperaciones.close()

        # Sumamos como última fila al total de debe y haber
        filasMovimientos.append(["Suma de Movimientos", "$" + str(debe), "$" + str(haber)])
        filasMovimientos.append(["", "Saldo Final: ", "$" + str(haber-debe)])
        
        # Creamos la Tabla
        crearTabla(columnasMovimientos, filasMovimientos)

    input("Presione Enter para continuar...")

'''''
Función para ser consumida por el resto de los módulos
Indicandole un Cliente obtenemos el saldo final de un cliente
'''''
def calcularSaldoFinal(clienteBuscar):
    # Definimos la variables acumuladoras
    debe = 0
    haber = 0

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
                if (int(cliente) == clienteBuscar):
                    # Sumamos Debe o Haber
                    if bool(int(operacion)) == True:
                        # Es una Factura, sumamos en Debe
                        debe = debe + int(monto)
                    else:
                        # Es un Recibo, sumamos en Haner
                        haber = haber + int(monto)

                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:            
            archivoOperaciones.close()

    # El saldo final de un cliente es el resultado de la resta
    # haber - debe
    return haber - debe

'''''
Función de uso interno para no mostrar reportes si no hay operaciones.
Además puede ser utilizado en el futuro con otros fines.

Al principio sólo pensé utilizarla para saber si hay una operación
devolviendo True a la lectura del primer registro y rompiendo el ciclo
pero me pareció útil tener un contador total de operaciones por si
a futuro lo necesitamos.
'''''
def cantidadOperaciones():
    cantidadOperaciones = 0

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
                cantidadOperaciones = cantidadOperaciones + 1

                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:            
            archivoOperaciones.close()

    return cantidadOperaciones

'''''
El total operativo es el cierre de caja
La diferencia entre el haber y el debe global (osea no solo de un cliente en especifico)
'''''
def totalOperativo():
    # Limpiamos la terminal 
    limpiarTerminal()

    print(" Total Operativo ".center(80,'-'))

    # Vamos a guardar cada monto en esta lista
    montoOperaciones = []

    # Leemos el archivo
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

                # Re-asignamos el valor de operación a tipo booleano
                operacion = bool(int(operacion))

                # Recordemos, si es una factura el saldo es negativo
                # Si es un recibo el saldo es positivo
                if (operacion == True):
                    # Es una factura, entonces lo convertimos a negativo
                    monto = int(monto) * -1
                else:
                    monto = int(monto)

                # Hacemos append a la lista montoOperaciones
                montoOperaciones.append(monto)

                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:            
            archivoOperaciones.close()

    # Perfecto, ahora debemos sumar todos los elementos para obtener el resultado operativo
    total = calcularOperativo(montoOperaciones)

    columnas = ["Total del Saldo Operativo"]
    filas = [["$" + str(total)]]

    # Lo mostramos de forma más linda como una tabla de una sola columna y una sola fila
    crearTabla(columnas, filas)

    input("Presione Enter para continuar...")

'''''
Necesitamos una función recursiva
Realmente es la única que se nos ocurrió
Lo debatimos durante horas
Qué sea lo que Dios quiera...

Enviamos la lista que contiene todos los montos
'''''
def calcularOperativo(lista):
    # Sumo los elementos de una lista de forma recursiva
    if len(lista) == 0:
        return 0
    else:
        # Con "1:"" lo que hacemos es ignorar el elemento actual y pasar al siguiente
        # Referencia: Página 23 de la PPT de Funciones Recursivas
        return lista[0] + calcularOperativo(lista[1:])