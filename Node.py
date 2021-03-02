class Node:
    def __init__(self,x,y, data):
        self.x = x
        self.y = y
        self.data = data
        self.next = None
    
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False
            