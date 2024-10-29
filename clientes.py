import random
from terminal import limpiarTerminal
from tablas import crearTabla
from operacionesExternas import obtenerOperacionesPorCliente

clientes = []
saldos = []
clientesCargados = False

def cargaClientes():
    limpiarTerminal()
    cargarLista(clientesCargados)

    print(" Carga de Clientes ".center(80,'-'))

    numeroCliente = 0
    while numeroCliente == 0:
        try:
            numeroCliente = int(input("Ingrese el Número de Cliente: "))
        except ValueError:
            print("ERROR: el Código de Cliente debe ser númerico")
        else:
            # El código de cliente proporcionado es un número
            if (verificarCliente(numeroCliente) == True):
                # El cliente existe, lo pedimos de nuevo
                numeroCliente = 0
    
    guardarCliente(numeroCliente)

def guardarCliente(numeroCliente):
    # Primero lo almacenamos en la listas
    clientes.append(numeroCliente)
    saldos.append(0)

    # Guardar en Archivo
    try:
        archivoCliente = open(r"clientes.csv","at")
    except IOError:
        print("ERROR al abrir el archivo de clientes")
    else:
        archivoCliente.write(str(numeroCliente) + ";" + str(0) + "\n")
        archivoCliente.close()

def consultarCliente():
    limpiarTerminal()
    cargarLista(clientesCargados)

    print(" Consultar Clientes ".center(80,'-'))
    numeroCliente = 0
    while numeroCliente == 0:
        try:
            numeroCliente = int(input("Ingrese el Número de Cliente: "))
        except ValueError:
            print("ERROR: el Código de Cliente debe ser númerico")
        else:
            # El código de cliente proporcionado es un número
            if (verificarCliente(numeroCliente) == False):
                # El cliente no existe, lo pedimos de nuevo
                numeroCliente = 0
    
    # Ya tengo el número de cliente en la variable numeroCliente
    # Ahora busco el saldo en la lista saldos
    indiceCliente = clientes.index(numeroCliente)
    print(f"El saldo del cliente {numeroCliente} es ${saldos[indiceCliente]}")

    input("Presione Enter para continuar")

def clienteMasCompras():
    limpiarTerminal()
    cargarLista(clientesCargados)

    print(" Cliente con más Compras ".center(80,'-'))

    # Variables acumuladoras
    indiceMasCompras = 0
    cantidadCompras = 0

    # Recorremos la lista de clientes
    for i in range(len(clientes)):
        # Vamos a aprovechar la función en el módulo de operaciones
        # para saber cuántas compras tiene el cliente actual
        comprasCliente = obtenerOperacionesPorCliente(clientes[i], True)
        
        if (i == 0):
            cantidadCompras = len(comprasCliente)
        elif (len(comprasCliente) > cantidadCompras):
            indiceMasCompras = i
            cantidadCompras = len(comprasCliente)

    print(f"El cliente {clientes[indiceMasCompras]} tiene {cantidadCompras} compras.")

    input("Presione Enter para continuar")

def clientesDeudores():
    limpiarTerminal()
    cargarLista(clientesCargados)

    # Lista donde almacenaremos los clientes deudores
    listaDeudores = []
    saldoDeudores  = []

    columnas = ["Cliente", "Saldo"]
    filas = []

    print(" Cliente/s más deudor/es ".center(80,'-'))

    # Recorremos la lista de clientes y consultamos su deuda
    for i in range(len(clientes)):
        # Obtener el saldo del cliente "i"
        saldoCliente = saldos[i]

        if (saldoCliente < 0):
            listaDeudores.append(i)
            saldoDeudores.append(saldoCliente)
            filas.append([i, "$" + str(saldoCliente)])

    # Mostramos en Tabla
    crearTabla(columnas, filas)

    input("Presione Enter para continuar")

def generarClientesRandom():
    limpiarTerminal()
    cargarLista(clientesCargados)

    print(" Generar Clientes al Azar ".center(80,'-'))

    # ¿Cuántos clientes vamos a generar?
    cantidadClientes = random.randint(1, 10)

    for i in range(cantidadClientes):
        # Generamos un Código de Cliente Random de 4 dígitos
        nuevoCliente = random.randint(1000, 9999)

        # Mientras el nuevo cliente exista generamos otro
        while nuevoCliente in clientes:
            # Generamos otro código porque el actual ya existe
            nuevoCliente = random.randint(1000, 9999)

        # Guardamos el nuevo cliente
        guardarCliente(nuevoCliente)

    print(f"Se han generado {cantidadClientes} nuevos clientes.")
    input("Presione Enter para continuar")

def cargarLista(clientesCargados):
    if (clientesCargados == False):
        # Leer archivo de clientes.csv
        try:
            archivoCliente = open(r"clientes.csv","rt")
        except IOError:
            print("ERROR al abrir el archivo de clientes")
        else:
            linea = archivoCliente.readline()

            while linea:
                cliente, saldo = linea.split(";")

                clientes.append(int(cliente))
                saldos.append(int(saldo))

                linea = archivoCliente.readline()

            clientesCargados = True
            archivoCliente.close()

def verificarCliente(buscarCliente):
    existeCliente = False

    # Leer archivo de clientes.csv
    try:
        archivoCliente = open(r"clientes.csv","rt")
    except IOError:
        print("ERROR al abrir el archivo de clientes")
    else:
        linea = archivoCliente.readline()

        while linea:
            cliente, saldo = linea.split(";")

            if (buscarCliente == int(cliente)):
                existeCliente = True

                # Cerramos el archivo antes de romper el ciclo
                archivoCliente.close()

                # Rompemos el ciclo
                break;

            linea = archivoCliente.readline()
        archivoCliente.close()

    return existeCliente

def actualizarSaldo(cliente, monto, sumar = True):
    cargarLista(clientesCargados)

    try:
        # Traemos el índice del cliente
        indiceCliente = clientes.index(cliente)
    except ValueError:
        # El cliente no existe
        print("Error: el cliente indicado no existe")
    else:
        # Obtenemos el saldo del cliente
        saldoCliente = saldos[indiceCliente]

        # Tenemos que sumar un monto o restarlo?
        if (sumar == True):
            # Sumamos el monto al saldo actual
            saldoCliente = saldoCliente  + monto
        else:
            # No hay que sumar, tenemos que restar
            saldoCliente = saldoCliente - monto

        # Actualizamos el saldo del cliente en la lista de saldos
        saldos[indiceCliente] = saldoCliente

        # Actualizamos el archivo escribiendo los datos modificados
        try:
            archivoCliente = open(r"clientes.csv","wt")
        except IOError:
            print("ERROR al abrir el archivo de clientes")
        else:
            # Recorremos toda la lista de clientes
            for i in range(len(clientes)):
                # Guardamos el cliente "i" y su nuevo saldo
                archivoCliente.write(str(clientes[i]) + ";" + str(saldos[i]) + "\n")

            archivoCliente.close()