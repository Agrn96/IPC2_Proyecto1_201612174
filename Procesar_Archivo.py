from Lista_Circular import CLista
import xml.etree.ElementTree as ET
ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\entrada1.xml"

def procesar():
    tree = ET.parse(ruta)
    root = tree.getroot()
    lista = CLista()
    lista_red = CLista()
    temp = lista
    temp_ = lista_red
    i=0

    #agregar informacion en Listas
    for nombre in root:
        #print(nombre.attrib['nombre'] + " " + nombre.attrib['n'] + " " + nombre.attrib['m'])
        for dato in root[i]:
            #print("NOMBRE: " + dato.attrib['x'] + " " + dato.attrib['y'] + " " + dato.text)
            if(int(dato.attrib['x']) > int(nombre.attrib['n']) or int(dato.attrib['y']) > int(nombre.attrib['m'])):
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

    temp_ = lista_red
    while(temp_.next != None):
        reducir(temp_)
        temp_ = temp_.next

    #iterador para la lista de listas circulares, mostrar las matrices
    temp = lista_red
    while(temp.next != None):
        temp.out()
        temp = temp.next


def reducir(lista):
    for i in range(1,int(lista.head.n)+1):
        for j in range(i+1,int(lista.head.n)+1):
            if(compare(lista,i,j)):
                add(lista,i,j)
                lista.pop(j)

def add(lista, i, j):
    temp = lista.head.next
    temp_ = lista.head.next
    try:
        while(temp.x != i):
            if(temp == lista.tail):
                return False
            temp = temp.next
    except:
        print("",end="")

    try:
        while(temp_.x != j):
            if(temp_ == lista.tail):
                return False
            temp_ = temp_.next
    except:
        print("",end="")

    for i in range(int(lista.head.m)):
        #print(temp.data, temp_.data)
        temp.data += temp_.data
        temp = temp.next
        temp_ = temp_.next

def compare(lista, i, j):
    temp = lista.head.next
    temp_ = lista.head.next
    try:
        while(temp.x != i):
            if(temp == lista.tail):
                return False
            temp = temp.next
    except:
        print("",end="")

    try:
        while(temp_.x != j):
            if(temp_ == lista.tail):
                return False
            temp_ = temp_.next
    except:
        print("",end="")
    
    for i in range(int(lista.head.m)):
        if((temp.data == 0 and temp_.data != 0) or (temp_.data == 0 and temp.data != 0)):
            return False
        temp = temp.next
        temp_ = temp_.next
    return True 

procesar()