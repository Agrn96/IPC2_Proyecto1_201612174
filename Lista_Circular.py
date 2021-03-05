from Node_info import Node_info
from Node_dato import Node_dato

class CLista:
    def __init__(self):
        self.head = Node_dato(None, None, None)
        self.tail = Node_dato(None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.next = None
        self.freq = Node_dato(None,None,None)

    def add_info(self, nombre, n, m):
        newNode = Node_info(nombre, n, m)
        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode
        
        self.freq = Node_dato(1,0,1)
        temp = self.freq
        for i in range(2,int(n)+1):
            temp_ = Node_dato(i,0,1)
            temp.next = temp_
            temp = temp.next

    
    def add_dato(self, x_, y_, data_):
        x = int(x_)
        y = int(y_)
        data = int(data_)
        newNode = Node_dato(x,y,data)
        if self.head.data is None:
            #add to the beginning of the list
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            newNode.next = self.head
        else:
            #add to the end of the list
            temp = self.head
            num = (int(temp.x)*100000) + (int(temp.y)*10)
            num_ = (int(x)*100000)+(int(y)*10)
            if(int(num_) < int(num)):
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif(self.head.next == self.tail):
                if(num_ > ((int(self.tail.x)*100000)+(int(self.tail.y)*10))):
                    newNode.next = self.head
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    self.head.next = newNode
                    newNode.next = self.tail
            else:
                while(int(num) < int(num_)):
                    if(temp.next == self.head):
                        temp.next = newNode
                        newNode.next = self.head
                        self.tail = newNode
                        temp = temp.next
                        break
                    temp = temp.next
                    num = (int(temp.next.x) * 100000) + (int(temp.next.y)*10)
                    
                if(temp.next != self.head):
                    newNode.next = temp.next
                    temp.next = newNode
                    

    def out(self):
        #Outputs the data in the list
        if self.head.data is None:
            print("No Data")
        else:
            print(self.head.data, self.head.n, self.head.m)
            temp = self.head.next
            while(temp != self.head):
                print(temp.data,temp.x,temp.y)
                temp = temp.next

    def pop(self,x_):
        x = int(x_)
        temp = self.head
        while(self.head.next.x != x):
            if(self.head == self.tail):
                break
            self.head = self.head.next
            
        
        if(x == self.tail.x):
            self.tail = self.head
            self.tail.next = temp
        else:
            for i in range(int(temp.m)):
                ran = self.head.next
                self.head.next = ran.next
        self.head = temp
    
    def freq_update(self,x_):
        x = int(x_)
        temp = self.freq
        while(temp.x != x):
            temp = temp.next
        temp.data += 1

