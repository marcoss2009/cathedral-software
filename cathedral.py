# Imports
import login
import menu


    
def main():
    
    # Diccionario con los usuarios y sus contraseñas
    cuentas = {
        "vendedor1": 1234,
        "vendedor2": 2345,
        "vendedor3": 3456,
        "vendedor4": 4567,
        "vendedor5": 5678}

    # Ingreso al sistema
    login.menuIngreso(cuentas)

    # Menú
    menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '='))

if __name__ == "__main__":
    main()