from tablas import crearTabla
from terminal import limpiarTerminal
from reportes import generarReporte

def cuentasCorrientesVendedor(cuentas):#chequear como recibo la lista de vendedores
    limpiarTerminal()
    
    print(" Cuentas Corrientes por Vendedor ".center(80, '-'))
    
    while True:
        try:
            vendedorBuscado = int(input("Ingrese el vendedor que desea buscar: "))
            
        except ValueError:
            print("Error: el número de vendedor solo puede contener números.")
            continue  # Volver al inicio del ciclo si hay un error de conversión
            
        else:
            if str(vendedorBuscado) in cuentas:
                break  # Salir del ciclo si el vendedor existe
            else:
                print("Error: el vendedor no existe")

            
    clienteLista = []
    operacionesLista = []
    saldoLista = []

    try:    
        archivo = open('operaciones.csv', mode='rt') #chequear nombre del archivo
    except IOError:
        print("Error al abrir el archivo")
    else:
        for linea in archivo:
            cliente, vendedor, operacion, monto = linea.split(";")
            
            # Convertir valores a enteros
            cliente = int(cliente)
            vendedor = int(vendedor)
            operacion = int(operacion)
            monto = int(monto)
            
            # Verificar si el vendedor coincide con el buscado
            if vendedor == vendedorBuscado:
                if cliente not in clienteLista:
                    clienteLista.append(cliente)
                    saldo_inicial = monto if operacion == 1 else -monto
                    saldoLista.append(saldo_inicial)
                    operacionesLista.append([operacion])
                else:
                    # Si el cliente ya está en la lista, actualizar saldo y operaciones
                    indice_cliente = clienteLista.index(cliente)
                    operacionesLista[indice_cliente].append(operacion)
                    
                    # Actualizar saldo según tipo de operación
                    if operacion == 1:
                        saldoLista[indice_cliente] -= monto
                    elif operacion == 0:
                        saldoLista[indice_cliente] += monto
                        
        print(f" Cuentas Corrientes del Vendedor: {vendedorBuscado} ".center(80, '-'))
        
        if len(clienteLista) == 0:
            print(" No hay movimientos para mostrar ".center(80, '-'))
        else:
            filas = []
            for i in range(len(clienteLista)):
                facturas = operacionesLista[i].count(1)  # Contar facturas (1)
                recibos = operacionesLista[i].count(0)   # Contar recibos (0)
                
                filas.append([clienteLista[i], facturas, recibos, saldoLista[i]])
                
            columnas = ["cliente","facturas","recibos","saldo"]
            
            crearTabla(columnas,filas)
        
    finally:
        archivo.close()
        
    input("Presione Enter para continuar...")
        
def ventasVendedores():
    limpiarTerminal()
    print(" Totales de Ventas por Vendedor ".center(80, '-'))
    
    try:    
        archivo = open(r'operaciones.csv', mode='rt') #chequear nombre del archivo
    except IOError:
        print("Error al abrir el archivo")
    else:
        ventasVendedores = [] #lista que almacena los ID de los vendedores
        mayorSaldo = [] #lista hermanada que almacena el total de ventas de cada vendedor
        try:
            for linea in archivo:
                cliente, vendedor, operacion, monto = linea.split(";")
                
                # Convertir valores a enteros
                cliente = int(cliente)
                vendedor = int(vendedor)
                operacion = int(operacion)
                monto = int(monto)
                
                if vendedor not in ventasVendedores:
                    ventasVendedores.append(vendedor)
                    if operacion == 0:
                        mayorSaldo.append(0)
                    else:
                        mayorSaldo.append(monto)
                else:
                    indiceVendedor = ventasVendedores.index(vendedor)
                    if operacion == 1:
                        mayorSaldo[indiceVendedor] = mayorSaldo[indiceVendedor] + monto
        finally:
            archivo.close()
            
        if len(mayorSaldo) > 0:  # Verifica que no esté vacío
            # Me tomo el atrevimiento de modificar el comportamiento de esta función a partir de acá
            # En vez de mostrar un único vendedor mostraremos a todos ordenados de mayor a menor por el monto de ventas totales
            # Inicializamos los parámetros para mostar una tabla
            columnas = ["Vendedor", "Monto de Ventas"]
            filas = []
            datosReporte = []

            # Empaquetamos las listas para después ordenarla
            listaVentas = [(mayorSaldo[i], ventasVendedores[i]) for i in range(len(mayorSaldo))]
            
            # Ordenamos de mayor a menor por monto de operación
            # Referencia: Página 70 PPT Clase 1
            listaVentas.sort(reverse=True)

            # Separar los valores en dos listas
            vendedoresOrdenados = [tupla[1] for tupla in listaVentas]
            montosOrdenados = [tupla[0] for tupla in listaVentas]

            # Iteramos y generamos las filas para la tabla
            for i in range(len(vendedoresOrdenados)):
                filas.append([vendedoresOrdenados[i], "$" + str(montosOrdenados[i])])
                datosReporte.append(str(vendedoresOrdenados[i]) + ";" + str(montosOrdenados[i]))

            # Mostramos en Tabla
            crearTabla(columnas, filas)

            # Generamos el archivo de reporte
            generarReporte(datosReporte, "vendedores_ventas")
        else:
            print("No se encontraron datos de ventas.")
            
    input("Presione Enter para continuar...")

#funcion lambda para verificar que el vendedor existe. 
#habria que corregir que reciba por parametro la lista de vendedores    
verificarVendedor = lambda buscado, cuentas: True if str(buscado) in cuentas else False