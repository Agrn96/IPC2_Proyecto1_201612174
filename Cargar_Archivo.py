from Lista_Circular import CLista
import xml.etree.ElementTree as ET

def cargar_Archivo(lista, lista_red):
    print("Ingrese la ruta del archivo:", end=" ");
    ruta = input();             # ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
    lista = CLista()            # Nueva Lista para guardar los datos en memoria
    lista_red = CLista()        # Copia de lista para reducir
    tree = ET.parse(ruta)       
    root = tree.getroot()
    temp = lista                # Iteradores para la lista circular
    temp_ = lista_red
    #agregar informacion en Listas
    i=0 # Contador para los matrizes
    for nombre in root:         # Iterar sobre los matrizes en el XML
        if(compare_name(lista,nombre.attrib['nombre'])==True):
                print("ERROR: Matriz: " + nombre.attrib['nombre'] + " ya existe")
                i+=1
                continue        # Si hay un matriz existente con el mismo nombre, se produce un error y sigue al siguiente matriz
        for dato in root[i]:    # Iterar sobre los datos en el matriz
            if(int(dato.attrib['x']) > int(nombre.attrib['n']) or int(dato.attrib['y']) > int(nombre.attrib['m'])):
                print("ERROR: Dato: "+ dato.text + "[" + dato.attrib['x'] + ", " + dato.attrib['y'] +"]esta fuera de rango" )
                continue    # Si los datos estan fuera de rango, se produce error y sigue al siguiente dato
            temp.add_dato(dato.attrib['x'],dato.attrib['y'],dato.text)      #Agrega el dato si esta en rango
            temp_.add_dato(dato.attrib['x'],dato.attrib['y'],dato.text)
        
        temp.add_info(nombre.attrib['nombre'], nombre.attrib['n'], nombre.attrib['m'])  # Agrega informacion del matriz al cabeza del lista circular
        temp_.add_info(nombre.attrib['nombre'], nombre.attrib['n'], nombre.attrib['m'])
        newLista = CLista()     # Crear una nueva lista
        newLista_ = CLista()
        temp.next = newLista    # Se apunte al nueva lista
        temp_.next = newLista_
        temp = temp.next        # Se itera al nueva lista
        temp_ = temp_.next
        i+=1                    
    return ruta, lista, lista_red

def compare_name(lista, nombre):    # Funcion para verificar si no hay un matriz existente con el mismo nombre
    temp = lista
    if(temp.head.data == None):
        return False

    while(temp.next != None):
        if(temp.head.data == nombre):
            return True
        temp = temp.next
    return False

