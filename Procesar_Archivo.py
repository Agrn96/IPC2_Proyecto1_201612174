from Lista_Circular import CLista
import xml.etree.ElementTree as ET
ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"

def procesar():
    tree = ET.parse(ruta)
    root = tree.getroot()
    lista = CLista()
    temp = lista
    i=0

    #agregar informacion en Listas
    for nombre in root:
        #print(nombre.attrib['nombre'] + " " + nombre.attrib['n'] + " " + nombre.attrib['m'])
        for dato in root[i]:
            #print("NOMBRE: " + dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            if(int(dato.attrib['x']) > int(nombre.attrib['n']) or int(dato.attrib['y']) > int(nombre.attrib['m'])):
                continue
            #print("Adding: " + nombre.attrib['nombre'] + " " + dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            temp.add_dato(nombre.attrib['nombre'],dato.attrib['x'],dato.attrib['y'],dato.text)
        
        temp.add_info(nombre.attrib['nombre'], nombre.attrib['n'], nombre.attrib['m'])
        newLista = CLista()
        temp.next = newLista
        temp = temp.next
        i+=1

    #iterador para la lista de listas circulares, mostrar las matrices
    temp = lista
    while(temp.next != None):
        temp.out()
        temp = temp.next


procesar()