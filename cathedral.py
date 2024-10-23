# Imports
import login
import menu
    
def main():
    # Ingreso al sistema
    login.menuIngreso()

    # Menú
    menu.mainMenu()

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '='))

if __name__ == "__main__":
    main()