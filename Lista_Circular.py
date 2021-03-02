import Node

class CLista:
    def __init__(self, n, m):
        self.head = Node.Node(None, None, None)
        self.tail = Node.Node(None, None, None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.n = n
        self.m = m
    
    def add(self, x, y, data):
        newNode = Node.Node(x,y,data)
        if self.head.data is None:
            #add to the beginning of the list
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        elif(((x==1) and (y==1)) and ((self.head.x != 1) and (self.head.y != 1))):
            #add beginning node to the start
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.tail.next = self.head
        else:
            while(self.head != self.tail):
                if(self.head.next.x == x and self.head.next.y == y):
                    break

                if(y==1):
                    if(x-self.head.x != 1):
                        self.head = self.head.next
                    elif(self.head.y != self.m):
                        self.head = self.head.next
                    else:
                        temp = self.head.next
                        self.head.next = newNode
                        newNode.next = temp
                else:
                    if(x != self.head.x):
                        self.head = self.head.next
                    if(y - self.head.y != 1):
                        self.head = self.head.next
                    else:
                        temp = self.head.next
                        self.head.next = newNode
                        newNode.next = temp

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