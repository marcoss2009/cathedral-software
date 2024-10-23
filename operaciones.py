from terminal import limpiarTerminal
from tablas import crearTabla
from clientes import verificarCliente
from vendedores import verificarVendedor
from random import randint

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
        archivoOperaciones.write(str(cliente) + ";" + vendedor + ";" + str(operacion) + ";" + str(monto) + "\n")
        archivoOperaciones.close()

def leerOperaciones(busqueda = "operacion", filtro = 0):
    filas = []

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
                    or (busqueda == "vendedor" and vendedor == filtro)
                ):
                    # Lo mostramos en Modo Tabla
                    # Al monto primero lo convertimos a int para eliminar el salto de línea
                    # y luego a texto nuevamente para poder concatenarlo con el símbolo "$"
                    filas.append([cliente, vendedor, ("Factura" if bool(int(operacion)) == True else "Recibo"), "$" + str(int(monto))])

                # Leemos la próxima línea
                linea = archivoOperaciones.readline()
        finally:            
            archivoOperaciones.close()
    
    # Creamos la Tabla
    # Primero definimos el nombre de las columnas
    columnasOperaciones = ["Cliente", "Vendedor", "Tipo de Operación", "Monto"]
    crearTabla(columnasOperaciones, filas)

def cargaOperaciones():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Carga de Operaciones ".center(80,'-'))

    '''''
    Solicitamos el Número de Cliente
    Creamos una excpción si el usuario ingresa algo distinto a un número
    Luego tendremos que verificar si este cliente existe con ayuda de alguna función del módulo de Clientes para tal fin

    Al igual que en el menú, cliente va a valer cero hasta que el cliente ingresado sea válido
    '''''
    cliente = 0
    while(cliente == 0):
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
                cliente = 0

    '''''
    Solicitamos el Vendedor
    No necesitaremos una excepción debido a que el vendedor es un valor string
    Luego tendremos que verificar si este vendedor existe con ayuda de alguna función del módulo de Vendedores para tal fin

    Al igual que en el menú, vendedor va a valer cero hasta que el vendedor ingresado sea válido
    '''''
    vendedor = 0
    while (vendedor == 0):
        vendedor = input("Ingrese el Vendedor: ")

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

def reporteFacturasRecibos():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Informe de Movimientos por Facturas y Recibos ".center(80,'-'))
    filtro = -1
    while (filtro == -1):
        try:
            filtro = int(input("Ingrese 0 para Recibos o 1 para Facturas: "))
        except ValueError:
            print("ERROR: El valor debe ser 0 para Recibos o 1 para Facturas")
        else:
            if filtro < 0 or filtro > 1:
                print("ERROR: El valor ingresado es incorrecto.")
                filtro = -1

    # Ahora vamos a leer todos los registros que cumplan con esta condición
    leerOperaciones("operacion", filtro)

    # Leemos cualquier tecla para volver al menú principal
    input("Presione una tecla para continuar...")

def reporteClienteVendedor():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Informe de Movimientos filtrados por Cliente y Vendedor ".center(80,'-'))
    filtro = -1
    while (filtro == -1):
        try:
            filtro = int(input("Ingrese 0 para filtrar por Cliente o 1 para filtrar por Vendedor: "))
        except ValueError:
            print("ERROR: El valor debe ser 0 para Cliente o 1 para Vendedor")
        else:
            if filtro < 0 or filtro > 1:
                print("ERROR: El valor ingresado es incorrecto.")
                filtro = -1

    '''''
    Wait a minute...
    Esto no termina acá lamentablamente...
    Ahora tenemos que verificar si el vendedor o cliente existe
    antes de empezar a filtrar los registros
    '''''
    valorBuscar = -1
    while valorBuscar == -1:
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
                    valorBuscar = 0
        else:
            # Filtramos por Vendedor
            valorBuscar = input("Ingrese el Vendedor: ")

            if verificarVendedor(valorBuscar) == False:
                print('ERROR: El Vendedor ingresado no existe')
                valorBuscar = 0

    # Ahora vamos a leer todos los registros que cumplan con esta condición
    leerOperaciones("vendedor" if bool(filtro) == True else "cliente", valorBuscar)

    # Leemos cualquier tecla para volver al menú principal
    input("Presione una tecla para continuar...")

def generarOperacionesRandom():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Generar Operaciones al Azar ".center(80,'-'))

    cantidadOperaciones = randint(2, 20)

    print(f"Se han generado {cantidadOperaciones} de operaciones al azar")
    input("Presione una tecla para continuar...")