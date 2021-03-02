import Menu
x = 0
while(x != 6):
    """Mientras x != 6, el menu sigue apareciendo
    """    
    print("")
    print("Menu Principal")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo Salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar Grafica")
    print("6. Salida")
    print("Choose Menu Option: ", end="\t")
    f = open("Ejemplo1.xml", "r")
    print(f.read())
    x = int(input())                #opcion del Menu
    Menu.menu(x)                    #Llamada al Menu utilizando el input del usuario
    