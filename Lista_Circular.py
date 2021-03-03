import Node

class CLista:
    def __init__(self):
        self.head = Node.Node(None, None, None, None)
        self.tail = Node.Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head
    
    def add(self, nombre, n_, m_, x, y, data):
        newNode = Node.Node(nombre,x,y,data)
        if self.head.data is None:
            print("Activated0")
            #add to the beginning of the list
            self.head = newNode
            self.head.next = self.head
            newNode.next = self.head
        elif(self.head.next == self.head):
            print("Activatedx")
            self.head.next = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            #add to the end of the list
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    def out(self):
        #Outputs the data in the list
        if self.head.data is None:
            print("No Data")
        elif self.head.next is self.head:
            print(self.head.data + " " + self.head.x)
            print(self.head.next.data + " " + self.head.next.x)
        else:
            temp_head = self.head
            print(temp_head.data,temp_head.x,temp_head.y)
            temp_head = temp_head.next
            while(temp_head != self.head):
                print(temp_head.data,temp_head.x,temp_head.y)
                # print(self.head.data)
                temp_head = temp_head.next