import Node

class CLista:
    def __init__(self):
        self.head = Node.Node(None, None, None)
        self.tail = Node.Node(None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head

    def set_Size(self,n,m):
        self.n = n
        self.m = m
    
    def add(self, x, y, data):
        newNode = Node.Node(x,y,data)
        if self.head.data is None:
            #add to the beginning of the list
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:     
            #add to the end of the list
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
            #sort after

    def out(self):
        #Outputs the data in the list
        if self.head.data is None:
            print("No Data")
        elif self.head.next is self.head:
            print(self.head.data)
        else:
            temp_head = self.head
            print(temp_head.data)
            temp_head = temp_head.next
            while(temp_head != self.head):
                print(temp_head.data)
                # print(self.head.data)
                temp_head = temp_head.next