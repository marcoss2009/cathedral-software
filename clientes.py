import random
from terminal import limpiarTerminal
from tablas import crearTabla
from operacionesExternas import obtenerOperacionesPorCliente
from reportes import generarReporte

def cargaClientes():
    limpiarTerminal()

    print(" Carga de Clientes ".center(80,'-'))

    while True:
        try:
            numeroCliente = int(input("Ingrese el Número de Cliente: "))
        except ValueError:
            print("ERROR: el Código de Cliente debe ser númerico")
        else:
            # El código de cliente proporcionado es un número
            if (verificarCliente(numeroCliente) == True):
                # El cliente existe, lo pedimos de nuevo
                print("El cliente ingresado ya existe. Ingrese uno nuevo.")
            else:
                # No existe el cliente, así que rompemos el ciclo y continuamos
                break;
    
    guardarCliente(numeroCliente)

def guardarCliente(numeroCliente):
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

    print(" Consultar Clientes ".center(80,'-'))

    # Tenemos suficiente cantidad de clientes para ejecutar esta operación?
    if cantidadClientes() <= 0:
        print(" No hay suficiente cantidad de datos para ejecutar esta operación. ".center(80,'-'))
    else:
        while True:
            try:
                numeroCliente = int(input("Ingrese el Número de Cliente: "))
            except ValueError:
                print("ERROR: el Código de Cliente debe ser númerico")
            else:
                # El código de cliente proporcionado es un número
                if (verificarCliente(numeroCliente) == True):
                    # El cliente existe, rompemos el ciclo
                    break
                else:
                    # El cliente no existe
                    print("El cliente indicado no existe")

        # Ya tengo el número de cliente en la variable numeroCliente
        # Ahora verificamos su saldo con la función saldoCliente
        print(f"El saldo del cliente {numeroCliente} es ${saldoCliente(numeroCliente)}")

    input("Presione Enter para continuar")

def clientesCompras():
    limpiarTerminal()

    print(" Cantidad de Compras por Cliente ".center(80,'-'))

    # Obtenemos la lista de clientes
    clientes = obtenerClientes()
    operaciones = [] # Lista hermanada donde almacenaremos la cantidad de operaciones de cada cliente

    # Inicializamos los parámetros para mostar una tabla
    columnas = ["Cliente", "Cantidad de Compras"]
    filas = []
    datosReporte = []

    # Iniciamos solo si tenemos clientes cargados
    if (len(clientes) > 0):
        # Recorremos la lista de clientes
        for i in range(len(clientes)):
            # Vamos a aprovechar la función en el módulo de operaciones
            # para saber cuántas compras tiene el cliente actual
            comprasCliente = obtenerOperacionesPorCliente(clientes[i], True)
            operaciones.append(len(comprasCliente))

        # Perfecto, tenemos la lista, ahora la empaquetamos para después ordenarla
        listaCompras = [(operaciones[i], clientes[i]) for i in range(len(operaciones))]

        # Ordenamos de mayor a menor por la cantidad de operaciones
        # Referencia: Página 70 PPT Clase 1
        listaCompras.sort(reverse=True)

        # Separar los valores en dos listas
        clientesOrdenados = [tupla[1] for tupla in listaCompras]
        cantidadesOrdenadas = [tupla[0] for tupla in listaCompras]
        
        # Iteramos y generamos las filas para la tabla
        for i in range(len(clientesOrdenados)):
            filas.append([clientesOrdenados[i], cantidadesOrdenadas[i]])
            datosReporte.append(str(clientesOrdenados[i]) + ";" + str(cantidadesOrdenadas[i]))

        # Mostramos en Tabla
        crearTabla(columnas, filas)

        # Generamos el archivo de reporte
        generarReporte(datosReporte, "clientes_compras")
    else:
        print("No hay suficientes datos para mostrar.")

    input("Presione Enter para continuar...")

def clientesDeudores():
    limpiarTerminal()
    print(" Cliente/s más deudor/es ".center(80,'-'))

    # Obtenemos la lista de clientes
    clientes = obtenerClientes()

    columnas = ["Cliente", "Saldo"]
    filas = []
    datosReporte = []

    # Recorremos la lista de clientes y consultamos su deuda
    for i in range(len(clientes)):
        # Obtener el saldo del cliente "i"
        clienteSaldo = saldoCliente(clientes[i])

        if (clienteSaldo < 0):
            filas.append([clientes[i], "$" + str(clienteSaldo)])
            datosReporte.append(str(clientes[i]) + ";" + str(clienteSaldo))

    # Mostramos en Tabla
    crearTabla(columnas, filas)

    # Generamos el archivo de reporte
    generarReporte(datosReporte, "clientes_deudores")

    input("Presione Enter para continuar...")

def generarClientesRandom():
    limpiarTerminal()

    print(" Generar Clientes al Azar ".center(80,'-'))

    # Obtenemos la lista de clientes
    clientes = obtenerClientes()

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

        # Por qué hacemos append a esta lista que solo está inicializada para esta función?
        # Porque si tenemos que generar un código nuevo debemos tener en cuenta los clientes random que ya fueron cargados
        # Ya que la lista por archivo se carga una sola vez
        clientes.append(nuevoCliente)

    print(f"Se han generado {cantidadClientes} nuevos clientes.")
    input("Presione Enter para continuar")

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

def saldoCliente(buscarCliente):
    saldoCliente = 0

    # Leer archivo de clientes.csv
    try:
        archivoCliente = open(r"clientes.csv","rt")
    except IOError:
        print("ERROR al abrir el archivo de clientes")
    else:
        try:
            linea = archivoCliente.readline()

            while linea:
                cliente, saldo = linea.split(";")

                if (buscarCliente == int(cliente)):
                    saldoCliente = int(saldo)

                    # Rompemos el ciclo
                    break;

                linea = archivoCliente.readline()
        finally:
            archivoCliente.close()

    return saldoCliente

# Sumar
# True = Recibo
# False = Factura
def actualizarSaldo(cliente, monto, factura = True):
    # Obtenemos la lista de clientes y de saldos
    clientes, saldos = obtenerClientesSaldos()

    # Chequeamos que el cliente existe
    if (cliente in clientes):
        # Obtenemos el saldo del cliente
        clienteSaldo = saldos[clientes.index(cliente)]

        # Tenemos que sumar un monto o restarlo?
        if (factura == True):
            # Restamos el monto al saldo actual ya que una factura es saldo negativo
            clienteSaldo = clienteSaldo - monto
        else:
            # No hay que restar, tenemos que sumar porque un recibo es saldo positivo
            clienteSaldo = clienteSaldo + monto

       # Actualizamos en la lista temporal que tenemos en esta función
        saldos[clientes.index(cliente)] = clienteSaldo

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
    else:
        print("Error: el cliente indicado no existe")

def cantidadClientes():
    clientes = obtenerClientes()

    # Devolvemos la cantidad de registros en la lista de clientes
    return len(clientes)

'''''
Para evitar utilizar listas locales utilizaremos esta función
para obtener los clientes cargados en el archivo y realizar comparaciones.
'''''
def obtenerClientes():
    clientes = []
    
    # Leer archivo de clientes.csv
    try:
        archivoCliente = open(r"clientes.csv","rt")
    except IOError:
        print("ERROR al abrir el archivo de clientes")
    else:
        try:
            linea = archivoCliente.readline()

            while linea:
                cliente, saldo = linea.split(";")
                clientes.append(int(cliente))

                linea = archivoCliente.readline()
        finally:
            archivoCliente.close()

    return clientes

def obtenerClientesSaldos():
    clientes = []
    saldos = []
    
    # Leer archivo de clientes.csv
    try:
        archivoCliente = open(r"clientes.csv","rt")
    except IOError:
        print("ERROR al abrir el archivo de clientes")
    else:
        try:
            linea = archivoCliente.readline()

            while linea:
                cliente, saldo = linea.split(";")
                clientes.append(int(cliente))
                saldos.append(int(saldo))

                linea = archivoCliente.readline()
        finally:
            archivoCliente.close()

    return clientes, saldos