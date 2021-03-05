from Lista_Circular import CLista

def procesar(lista_red):
    temp_ = lista_red
    while(temp_.next != None):
        reducir(temp_)
        temp_ = temp_.next

    #iterador para la lista de listas circulares, mostrar las matrices
    temp = lista_red
    while(temp.next != None):
        print("PA")
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
    while(temp.x != i):
        if(temp == lista.tail):
            return False
        temp = temp.next
    
    
    while(temp_.x != j):
        if(temp_ == lista.tail):
            return False
        temp_ = temp_.next
    

    for i in range(int(lista.head.m)):
        temp.data += temp_.data
        temp = temp.next
        temp_ = temp_.next

def compare(lista, i, j):
    temp = lista.head.next
    temp_ = lista.head.next
    
    while(temp.x != i):
        if(temp == lista.tail):
            return False
        temp = temp.next

    
    while(temp_.x != j):
        if(temp_ == lista.tail):
            return False
        temp_ = temp_.next
    
    
    for i in range(int(lista.head.m)):
        if((temp.data == 0 and temp_.data != 0) or (temp_.data == 0 and temp.data != 0)):
            return False
        temp = temp.next
        temp_ = temp_.next
    return True 