import Node

class CLista:
    def __init__(self):
        self.head = Node.Node(None, None, None, None)
        self.tail = Node.Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head
    
    def add(self, nombre, x, y, data):
        newNode = Node.Node(nombre,x,y,data)
        if self.head.data is None:
            #add to the beginning of the list
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            newNode.next = self.head
        else:
            #add to the end of the list
            temp = self.head
            num = (int(temp.x)*10) + int(temp.y)
            num_ = (int(x)*10)+int(y)
            if(num_ < num):
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif(self.head.next == self.tail):
                if(num_ > ((int(self.tail.x)*10)+int(self.tail.y))):
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
                    num = (int(temp.next.x) * 10) + int(temp.next.y)
                if(temp.next != self.head):
                    newNode.next = temp.next
                    temp.next = newNode
                    

    def out(self):
        #Outputs the data in the list
        if self.head.data is None:
            print("No Data")
        elif self.head.next is self.head:
            print(self.head.data + " " + self.head.x)
        else:
            while(self.head != self.tail):
                print(self.head.data,self.head.x,self.head.y)
                self.head = self.head.next
            print(self.tail.data,self.tail.x,self.tail.y)