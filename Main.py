import Menu
from Lista_Circular import CLista
lista = CLista()
lista_red = CLista()
x = 0
while(x != 6):
    """Mientras x != 6, el menu sigue apareciendo
    """     

    print("")
    print("Menu Principal")
    print("1. Cargar Archivo")
    #D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml
    print("2. Procesar Archivo")
    print("3. Escribir Archivo Salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar Grafica")
    print("6. Salida")
    print("Choose Menu Option: ", end="\t")

    #f = open(ruta1, "r")
    #print(f.read())
    x = int(input())                #opcion del Menu
    Menu.menu(x,lista,lista_red)                    #Llamada al Menu utilizando el input del usuario
    