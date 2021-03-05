from graphviz import Digraph
import os
os.environ["PATH"]  += os.pathsep + 'D:/Program Files (x86)/Graphviz/bin/'

def generate(lista):

    dot = Digraph(comment='Lista Circular, Matriz: ' + str(lista.head.data))
    dot #doctestL +ELLIPSIS

    dot.node('A','Matrices')
    dot.node('B',lista.head.data)
    dot.node('C',lista.head.n)
    dot.node('D',lista.head.m)
    x = int(lista.head.n)
    y = int(lista.head.m)
    temp = lista.head.next
    while(temp != lista.head):
        name = 'E' + str(int(temp.x)*100) + str(temp.y)
        dot.node(name,str(temp.data))
        if(int(temp.x) == 1):
            dot.edge('B','E' + str(int(temp.x)*100) + str(int(temp.y)))
        else:
            dot.edge('E' + str((int(temp.x)-1)*100) + str(int(temp.y)),'E' + str(int(temp.x)*100) + str(temp.y))
        temp = temp.next

    dot.edges(['AB','BC','BD'])
    dot.render('Grafica.dot', view=True)