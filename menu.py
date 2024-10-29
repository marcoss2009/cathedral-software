import clientes
import vendedores
import operaciones
from terminal import limpiarTerminal

def mainMenu():
    opcion = selectMainMenu()

    if (opcion == 1):
        menuClientes()

    if (opcion == 2):
        menuVendedores()

    if (opcion == 3):
        menuOperaciones()

    if (opcion == 4):
        menuReportes()

    # Limpiamos la terminal
    limpiarTerminal()

def selectMainMenu():
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Seleccione una opción para comenzar ".center(80,'-'))
    print("1. Ingreso al Módulo de Clientes")
    print("2. Ingreso al Módulo de Vendedores")
    print("3. Ingreso al Módulo de Operaciones")
    print("4. Reportes")
    print("5. Salir del Sistema")

    
    opcion = 0 # Preguntar a la profe si esta aberración está bien para evitar utilizar else...
    while opcion == 0:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion < 1 or opcion > 5):
                opcion = 0

    return opcion

def menuClientes():
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Clientes ".center(80,'-'))
    print("1. Carga de Clientes")
    print("2. Consultar Clientes")
    print("3. Generar Clientes al Azar")
    print("4. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 4):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        clientes.cargaClientes()
    
    if opcion == 2:
        clientes.consultarCliente()

    if opcion == 3:
        clientes.generarClientesRandom()

    mainMenu()

def menuVendedores():
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Vendedores ".center(80,'-'))
    print("1. Cuentas Corrientes por Vendedor")
    print("2. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 2):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vendedores.cuentasCorrientesVendedor()
    
    mainMenu()

def menuOperaciones():
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Operaciones ".center(80,'-'))
    print("1. Carga de Operaciones")
    print("2. Generar Operaciones al Azar")
    print("3. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 3):
        opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        operaciones.cargaOperaciones()

    if opcion == 2:
        operaciones.generarOperacionesRandom()
    
    mainMenu()

def menuReportes():
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Reportes ".center(80,'-'))
    print("1. Vendedor con más Ventas")
    print("2. Cliente con más Compras")
    print("3. Cliente/s más deudor/es")
    print("4. Informe de Movimientos filtrados por Facturas y Recibos")
    print("5. Informe de Movimientos filtrados por Cliente y Vendedor")
    print("6. Vista de Cuenta Corriente por Cliente")
    print("7. Volver al Menú Principal")

    opcion = int(input("Seleccione una opción: "))

    while (opcion < 1 or opcion > 7):
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
        operaciones.cuentaCorriente()
    
    mainMenu()