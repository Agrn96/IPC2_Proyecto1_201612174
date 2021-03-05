from Lista_Circular import CLista

def procesar(lista_red):
    temp_ = lista_red
    while(temp_.next != None):
        print("\nREDUCIENDO: " + temp_.head.data + "\n")
        reducir(temp_)
        temp_ = temp_.next

def reducir(lista):
    for i in range(1,int(lista.head.n)+1):
        print("Comparando la fila: " + str(i) + " con las otras filas.")
        for j in range(i+1,int(lista.head.n)+1):
            if(compare(lista,i,j)):
                print("Sumando Fila: " + str(i) + " == Fila: " + str(j))
                add(lista,i,j)
                lista.freq_update(i,1)
                lista.freq_update(j,-1)
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