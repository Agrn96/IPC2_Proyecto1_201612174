from Procesar_Archivo import procesar
from Cargar_Archivo import cargar_Archivo
from tkinter import *
from tkinter import filedialog

def menu(x):
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        ruta = cargar_Archivo()
        print("Opcion 1 terminado, ruta es: ", end=" ");
        #Testing
        print(ruta); 
        f = open(ruta, "r")
        #print(f.read())
        #f.close();
        #/Testing
    elif(x == 2):
        procesar();
    elif(x == 3):
        print("Placeholder")
    elif(x == 4): # Menu Opcion 4: Mostrar datos del estudiante
        print("\nAlberto Gabriel Reyes Ning\n201612174\nIPC2-A\nIngenieria en Ciencias y Sistemas\n4to Semestre")
    elif(x == 5):
        print("Placeholder")
    elif(x == 6):
        print("Saliendo del applicacion")
        raise SystemExit(0)  # Se cierra la aplicacion
    else:
        print("Opcion Invalida")