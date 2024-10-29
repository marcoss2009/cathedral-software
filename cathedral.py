# Imports
import login
import menu
from vendedores import traerVendedores
    
def main():
    # Diccionario con los usuarios y sus contraseñas
    cuentas = traerVendedores()

    # Ingreso al sistema
    login.menuIngreso(cuentas)

    # Menú
    menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '='))

if __name__ == "__main__":
    main()