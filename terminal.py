# Importamos la librería OS para acceder a funciones del sistema operativo
from os import system, name

def limpiarTerminal():
    # Verifiquemos si estamos en Windows (NT = Windows Kernel)
    if name == "nt":
        system('cls')
    else:
        # Estamos en UNIX, osea, mac, linux, etc.
        system('clear')

    print(" Cathedral Software ".center(80, '='))