import clientes
import vendedores
import operaciones
from terminal import limpiarTerminal

def mainMenu(cuentas):
    opcion = selectMainMenu()

    if (opcion == 1):
        menuClientes(cuentas)

    if (opcion == 2):
        menuVendedores(cuentas)

    if (opcion == 3):
        menuOperaciones(cuentas)

    if (opcion == 4):
        menuReportes(cuentas)

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

    while True:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion >= 1 and opcion <= 5):
                # La opción está entre 1 y 5, rompemos el ciclo y continuamos
                break;

    return opcion

def menuClientes(cuentas):
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Clientes ".center(80,'-'))
    print("1. Carga de Clientes")
    print("2. Consultar Clientes")
    print("3. Generar Clientes al Azar")
    print("4. Volver al Menú Principal")

    while True:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion >= 1 and opcion <= 4):
                # La opción está entre 1 y 4, rompemos el ciclo y continuamos
                break;

    if opcion == 1:
        clientes.cargaClientes()
    
    if opcion == 2:
        clientes.consultarCliente()

    if opcion == 3:
        clientes.generarClientesRandom()

    mainMenu(cuentas)

def menuVendedores(cuentas):
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Vendedores ".center(80,'-'))
    print("1. Cuentas Corrientes por Vendedor")
    print("2. Volver al Menú Principal")

    while True:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion >= 1 and opcion <= 2):
                # La opción está entre 1 y 2, rompemos el ciclo y continuamos
                break;

    if opcion == 1:
        vendedores.cuentasCorrientesVendedor(cuentas)
    
    mainMenu(cuentas)

def menuOperaciones(cuentas):
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Operaciones ".center(80,'-'))
    print("1. Carga de Operaciones")
    print("2. Generar Operaciones al Azar")
    print("3. Volver al Menú Principal")

    while True:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion >= 1 and opcion <= 3):
                # La opción está entre 1 y 3, rompemos el ciclo y continuamos
                break;

    if opcion == 1:
        operaciones.cargaOperaciones(cuentas)

    if opcion == 2:
        operaciones.generarOperacionesRandom()
    
    mainMenu(cuentas)

def menuReportes(cuentas):
    # Limpiamos la terminal
    limpiarTerminal()

    # Seleccione una opción
    print(" Módulo de Reportes ".center(80,'-'))
    print("1. Totales de Ventas por Vendedor")
    print("2. Cantidad de Compras por Clientes")
    print("3. Clientes Deudores")
    print("4. Informe de Movimientos filtrados por Facturas y Recibos")
    print("5. Informe de Movimientos filtrados por Cliente y Vendedor")
    print("6. Vista de Cuenta Corriente por Cliente")
    print("7. Calcular el Total Operativo")
    print("8. Volver al Menú Principal")

    while True:
        # Manejo de Excepciones
        # Solo podemos ingresar números...
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError: # El usuario ingresó algo distinto a un número, mostramos el error y continuamos
            print('La opción para comenzar debe ser un número.')
        else:
            if (opcion >= 1 and opcion <= 8):
                # La opción está entre 1 y 8, rompemos el ciclo y continuamos
                break;

    if opcion == 1:
        vendedores.ventasVendedores()

    if opcion == 2:
        clientes.clientesCompras()

    if opcion == 3:
        clientes.clientesDeudores()

    if opcion == 4:
        operaciones.reporteFacturasRecibos()

    if opcion == 5:
        operaciones.reporteClienteVendedor(cuentas)

    if opcion == 6:
        operaciones.cuentaCorriente()
    
    if opcion == 7:
        operaciones.totalOperativo()
    
    mainMenu(cuentas)