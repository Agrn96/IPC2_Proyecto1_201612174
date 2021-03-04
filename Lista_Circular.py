from Node_info import Node_info
from Node_dato import Node_dato

class CLista:
    def __init__(self):
        self.head = Node_dato(None, None, None, None)
        self.tail = Node_dato(None, None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.next = None

    def add_info(self, nombre, n, m):
        newNode = Node_info(nombre, n, m)
        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode
    
    def add_dato(self, nombre, x, y, data):
        newNode = Node_dato(nombre,x,y,data)
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
                #num = ((int(temp.next.x)) * 10) + int(temp.next.y)
                
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
                    #print(num, num_)
                    newNode.next = temp.next
                    temp.next = newNode
                    

    def out(self):
        #Outputs the data in the list
        if self.head.data is None:
            print("No Data")
        else:
            print(self.head.data, self.head.n, self.head.m)
            self.head = self.head.next
            while(self.head != self.tail):
                print(self.head.data,self.head.x,self.head.y)
                self.head = self.head.next
            print(self.tail.data,self.tail.x,self.tail.y)