class Node_info:
    #Clase para guardar informacion del matric, se puede usar Node_dato.py tambien
    def __init__(self,nombre, n,m):
        self.data = nombre
        self.n = n
        self.m = m
        self.next = None