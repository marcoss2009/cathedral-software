import login
import menu

def main():
    # Diccionario con los usuarios y sus contraseñas
    cuentas = {
        "1000": 1234,
        "1001": 2345,
        "1002": 3456,
        "1003": 4567,
        "1004": 5678
    }

    # Ingreso al sistema
    login.menuIngreso(cuentas)

    # Menú
    menu.mainMenu(cuentas)

    print(" Gracias por utilizar Cathedral Software ".center(80, '-'))
    print(" π".rjust(80, '='))

if __name__ == "__main__":
    main()