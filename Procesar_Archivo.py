from typing import ClassVar
from Lista_Circular import CLista
import xml.etree.ElementTree as ET
ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
def procesar():
    tree = ET.parse(ruta)
    root = tree.getroot()
    lista = CLista()
    i=0
    for nombre in root:
        print(nombre.attrib['nombre'] + " " + nombre.attrib['n'] + " " + nombre.attrib['m'])
        for dato in root[i]:
            print("NOMBRE: " + dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            if(dato.attrib['x'] > nombre.attrib['n'] or dato.attrib['y'] > nombre.attrib['m']):
                print("skipped")
                continue

            print("Adding: " + nombre.attrib['nombre'] + " " + dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            lista.add(nombre.attrib['nombre'],nombre.attrib['n'],nombre.attrib['m'],dato.attrib['x'],dato.attrib['y'],dato.text)
        print("xxx")
        i+=1
    print("YYY")
    lista.out()
procesar()