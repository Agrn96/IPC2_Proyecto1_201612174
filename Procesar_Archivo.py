from Lista_Circular import CLista
import xml.etree.ElementTree as ET
ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
def procesar():
    #print("Test2");
    #print(ruta);
    tree = ET.parse(ruta)
    root = tree.getroot()
    #for dato in root:
    #    print(dato.attrib)
    #print(root.attrib)
    #print(root[0][0].text)
    #for child in root:
    #    rank = child.tag
    #    name = child.attrib
    #   print(rank,name)
    
    #for dato in root[1]:
        #print(dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
        #x = dato.attrib['x']
        #print(x);
    i=0
    for nombre in root:
        print(nombre.attrib['nombre'] + " " + nombre.attrib['n'] + " " + nombre.attrib['m'])
        for dato in root[i]:
            print(dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            #x = int(dato.attrib['x'])
            #print(x);
        print("xxx")
        i+=1

        #print(root[0][1].text)
    #Lista = CLista(5,4)
    

procesar()