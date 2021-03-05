from Lista_Circular import CLista
import xml.etree.ElementTree as ET

def cargar_Archivo(lista, lista_red):
    print("Ingrese la ruta del archivo:", end=" ");
    ruta = input();             #ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
    lista = CLista()
    lista_red = CLista()
    tree = ET.parse(ruta)
    root = tree.getroot()
    temp = lista
    temp_ = lista_red
    #agregar informacion en Listas
    i=0
    for nombre in root:
        if(compare_name(lista,nombre.attrib['nombre'])==True):
                print("ERROR: Matriz: " + nombre.attrib['nombre'] + " ya existe")
                i+=1
                continue
        for dato in root[i]:  
            if(int(dato.attrib['x']) > int(nombre.attrib['n']) or int(dato.attrib['y']) > int(nombre.attrib['m'])):
                print("ERROR: Dato: "+ dato.text + "[" + dato.attrib['x'] + ", " + dato.attrib['y'] +"]esta fuera de rango" )
                continue
            temp.add_dato(dato.attrib['x'],dato.attrib['y'],dato.text)
            temp_.add_dato(dato.attrib['x'],dato.attrib['y'],dato.text)
        
        temp.add_info(nombre.attrib['nombre'], nombre.attrib['n'], nombre.attrib['m'])
        temp_.add_info(nombre.attrib['nombre'], nombre.attrib['n'], nombre.attrib['m'])
        newLista = CLista()
        newLista_ = CLista()
        temp.next = newLista
        temp_.next = newLista_
        temp = temp.next
        temp_ = temp_.next
        i+=1
    return ruta, lista, lista_red

def compare_name(lista, nombre):
    temp = lista
    if(temp.head.data == None):
        return False

    while(temp.next != None):
        if(temp.head.data == nombre):
            return True
        temp = temp.next
    return False

