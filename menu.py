import clientes
import vendedores
import operaciones

def mainMenu():
    opcion = selectMainMenu()

    while (opcion != 5):
        if (opcion == 1):
            menuClientes()

        if (opcion == 2):
            menuVendedores()

        if (opcion == 3):
            menuOperaciones()

        if (opcion == 4):
            menuReportes()

        opcion = selectMainMenu()

def selectMainMenu():
    # Seleccione una opción
    print(" Seleccione una opción para comenzar ".center(80,'-'))
    print("1. Ingreso al Módulo de Clientes")
    print("2. Ingreso al Módulo de Vendedores")
    print("3. Ingreso al Módulo de Operaciones")
    print("4. Reportes")
    print("5. Salir del Sistema")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 5):
        opcion = int(input("Seleccione una opción: "))

    return opcion

def menuClientes():
    # Seleccione una opción
    print(" Módulo de Clientes ".center(80,'-'))
    print("1. Carga de Clientes")
    print("2. Consultar Clientes")
    print("3. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 3):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        clientes.cargaClientes()
    
    if opcion == 2:
        clientes.consultarCliente()

    if opcion == 3:
        mainMenu()

def menuVendedores():
    # Seleccione una opción
    print(" Módulo de Vendedores ".center(80,'-'))
    print("1. Cuentas Corrientes por Vendedor")
    print("2. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 2):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vendedores.cuentasCorrientesVendedor()
    
    if opcion == 2:
        mainMenu()

def menuOperaciones():
    # Seleccione una opción
    print(" Módulo de Operaciones ".center(80,'-'))
    print("1. Cuentas Corrientes por Vendedor")
    print("2. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 2):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vendedores.cuentasCorrientesVendedor()
    
    if opcion == 2:
        mainMenu()

def menuReportes():
    # Seleccione una opción
    print(" Módulo de Reportes ".center(80,'-'))
    print("1. Vendedor con más Ventas")
    print("2. Cliente con más Compras")
    print("3. Cliente/s más deudor/es")
    print("4. Informe de Movimientos filtrados por Facturas y Recibos")
    print("5. Informe de Movimientos filtrados por Cliente y Vendedor")
    print("6. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 6):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vendedores.vendedorConMasVentas()

    if opcion == 2:
        clientes.clienteMasCompras()

    if opcion == 3:
        clientes.clientesDeudores()

    if opcion == 4:
        operaciones.reporteFacturasRecibos()

    if opcion == 5:
        operaciones.reporteClienteVendedor()
    
    if opcion == 6:
        mainMenu()