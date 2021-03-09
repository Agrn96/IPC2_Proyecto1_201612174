from tkinter.constants import E
from Menu import menu
from Lista_Circular import CLista
lista = CLista()
lista_red = CLista()

def main(lista, lista_red): 
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

        try:
            x = int(input())                                #opcion del Menu
            lista, lista_red = menu(x, lista, lista_red)    #Llamada al Menu utilizando el input del usuario
        except:
            print("ERROR: Opcion Invalido")
main(lista, lista_red)