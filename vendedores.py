def cuentasCorrientesVendedor(vendedores): #chequear como recibo la lista de vendedores
    print("1. Cuentas Corrientes por Vendedor")
    
    while True:
        try:
            vendedorBuscado = int(input("Ingrese el vendedor que desea buscar: "))
            
        except ValueError:
            print("Error: el número de vendedor solo puede contener números.")
            continue  # Volver al inicio del ciclo si hay un error de conversión
            
        else:
            if vendedorBuscado in vendedores:
                print("Vendedor encontrado.")
                break  # Salir del ciclo si el vendedor existe
            else:
                print("Error: el vendedor no existe")

            
        clienteLista = []
        operacionesLista = []
        saldoLista = []

        try:    
            archivo = open('prueba.txt', mode='r') #chequear nombre del archivo
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
                            saldoLista[indice_cliente] += monto
                        elif operacion == 0:
                            saldoLista[indice_cliente] -= monto
                            
            print(f" Cuentas Corrientes del Vendedor: {vendedorBuscado} ".center(80, '-'))
            
            if len(clienteLista) == 0:
                print(" No hay movimientos para mostrar ".center(80, '-'))
            else:
                for i in range(len(clienteLista)):
                    facturas = operacionesLista[i].count(1)  # Contar facturas (1)
                    recibos = operacionesLista[i].count(0)   # Contar recibos (0)
                    print("cliente: ",clienteLista[i])
                    print("Cantidad de facturas: ", facturas)
                    print("Cantidad de recibos: ", recibos)
                    print("Saldo total del cliente: $", saldoLista[i])
                    print("-" * 40)
            
        finally:
            archivo.close()


def vendedorConMasVentas():
    print("1. Vendedor con más Ventas")
    
    try:    
        archivo = open('prueba.txt', mode='r') #chequear nombre del archivo
    except IOError:
        print("Error al abrir el archivo")
    else:
        
        ventasVendedores = [] #lista que almacena los ID de los vendedores
        mayorSaldo = [] #lista hermanada que almacena el total de ventas de cada vendedor
        
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
             
        mayorVendedor = max(mayorSaldo)
        indiceMayorVendedor = mayorSaldo.index(mayorVendedor)
        
        if mayorSaldo:  # Verifica que no esté vacío
            mayorVendedor = max(mayorSaldo)
            indiceMayorVendedor = mayorSaldo.index(mayorVendedor)
        
            print(f"El vendedor con más ventas es el vendedor numero: {ventasVendedores[indiceMayorVendedor]} con una suma de ventas de ${mayorVendedor}")
        else:
            print("No se encontraron datos de ventas.")
            
            

#funcion lambda para verificar que el vendedor existe. 
#habria que corregir que reciba por parametro la lista de vendedores    
verificarVendedor = lambda buscado: True if buscado in [1000, 1001, 1002, 1003, 1004] else False
    


                    
