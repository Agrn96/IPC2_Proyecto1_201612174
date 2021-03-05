import xml.etree.ElementTree as ET

def salida_Archivo(lista_):
    temp = lista_
    try:
        print("Escribir una ruta especifica: ", end="")
        ruta = input()
    except:
        print("Hay un error con la ruta de salida")
    
    root = ET.Element("matrices")
    while(temp.next != None):
        matriz = ET.SubElement(root, "matriz", nombre = temp.head.data, n = temp.head.n, m = temp.head.m)
        i = 1
        j = 1
        m = int(temp.head.m)
        temp.head = temp.head.next
        while(temp.head != temp.tail.next):
            ET.SubElement(matriz, "dato", x = str(i), y = str(j)).text = str(temp.head.data)
            j += 1
            if(j>m):
                j = 1
                i += 1
            temp.head = temp.head.next
        matriz.set('n',str(i-1))
        while(temp.freq != None):
            if(temp.freq.data != 0):
                ET.SubElement(matriz, "frecuencia", g = str(temp.freq.x)).text = str(temp.freq.data)
            temp.freq = temp.freq.next
        temp = temp.next

    tree = ET.ElementTree(root)
    tree.write(ruta)