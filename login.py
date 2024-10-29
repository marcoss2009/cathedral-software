from terminal import limpiarTerminal

def menuIngreso(cuentas):
    # Limpiamos la terminal
    limpiarTerminal()
    
    print(" Ingreso al Sistema ".center(80,'-'))
    
    while True: 
        usuario = input("Ingrese usuario: ")
        
        if usuario in cuentas:  # Verifica si el usuario está en el diccionario
            break  # Sale del bucle si el usuario es válido
        else:
            print("Usuario no encontrado. Ingrese nuevamente.")  # Mensaje si el usuario no está en cuentas

    while True:  # Si el usuario está en cuentas, inicia otro bucle para la contraseña
        try:
            clave = int(input("Ingrese clave: "))  
        except ValueError:
            print("Error, la clave debe ser numérica.")  # Maneja el error si no se ingresa un número
            continue  # Vuelve a solicitar la clave
        
        else:
            if clave != cuentas[usuario]:  
                print("Error. Clave incorrecta")
            else:
                break
        