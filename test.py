try:
    archivoPrueba = open("operaciones.csv","wt")
except IOError:
    print("no se pudo crear el archivo")
else:
    archivoPrueba.write("8000"+";"+"1000"+";"+"0"+";"+"1000"+"\n"
                        "8000"+";"+"1000"+";"+"1"+";"+"1000"+"\n"
                        "9001"+";"+"1001"+";"+"1"+";"+"9000"+"\n"
                        "502"+";"+"1001"+";"+"1"+";"+"9000"+"\n"
                        "9001"+";"+"1001"+";"+"0"+";"+"9000"+"\n")
                        
    archivoPrueba.close()