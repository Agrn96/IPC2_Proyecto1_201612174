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


    prettify(root)
    tree = ET.ElementTree(root)
    tree.write(ruta, encoding='UTF-8', xml_declaration=True)

#https://stackoverflow.com/a/38573964 Codigo hecho por el Usuario Nacitar Sevaht, utilizado para que el archivo de xml sea ligible 
def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings