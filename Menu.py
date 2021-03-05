from Procesar_Archivo import procesar
from Salida_Archivo import salida_Archivo
from Cargar_Archivo import cargar_Archivo
from Generar_grafica import generate
from tkinter import *
from tkinter import filedialog

def menu(x, lista, lista_red):
    temp = lista
    temp_ = lista_red
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        ruta, lista, lista_red = cargar_Archivo(lista, lista_red)
        print("Opcion 1 terminado, ruta es: " + ruta);
        return lista,lista_red
    elif(x == 2):
        procesar(temp_);
        return lista,lista_red
    elif(x == 3):
        salida_Archivo(temp_)
        print("Se escribio el archivo satisfactorio")
        return lista,lista_red
    elif(x == 4): # Menu Opcion 4: Mostrar datos del estudiante
        print("\nAlberto Gabriel Reyes Ning\n201612174\nIPC2-A\nIngenieria en Ciencias y Sistemas\n4to Semestre")
        return lista,lista_red
    elif(x == 5):
        # Imprimir opciones
        ran = temp
        i = 1
        while(ran.next != None):
            print(str(i) + ": ", end="")
            print(ran.head.data)
            ran = ran.next
            i += 1
        print("\nChoose List: ", end="")
        l = int(input())
        # Iterar al grafica selecionado
        for i in range(1,l):
            temp = temp.next
        # Generar la grafica selecionado
        generate(temp)
        return lista,lista_red
    elif(x == 6):
        print("Saliendo del applicacion")
        raise SystemExit(0)  # Se cierra la aplicacion
    else:
        print("Opcion Invalida")