from graphviz import Digraph
import os
os.environ["PATH"]  += os.pathsep + 'D:/Program Files (x86)/Graphviz/bin/'

def generate(lista):

    dot = Digraph(comment='Lista Circular, Matric: ' + lista.head.data)
    dot #doctestL +ELLIPSIS

    dot.node('A','Matrices')
    dot.node('B',lista.head.data)
    dot.node('C',lista.head.n)
    dot.node('D',lista.head.m)
    x = int(lista.head.n)
    y = int(lista.head.m)
    temp = lista.head.next
    print(x,y)

    while(temp != lista.head):
        name = 'E' + str(int(temp.x)*100) + str(temp.y)
        dot.node(name,str(temp.data))
        if(int(temp.y) == 1):
            dot.edge('B','E' + str(int(temp.x)*100) + '1')
        else:
            dot.edge('E' + str(int(temp.x)*100) + str(int(temp.y)-1),'E' + str(int(temp.x)*100) + str(temp.y))
        temp = temp.next
        
    dot.edges(['AB','BC','BD'])
    dot.render('Salida.dot', view=True)