import pydot as pgv

from ast import NodeVisitor

class DotVisitor(NodeVisitor):

        '''
        Crea archivo tipo 'dot' para Graphiz
        '''
        def __init__(self):
                self.dot =pgv.Dot('AST',graph_type='digraph')
                '''creamos un obj del tipo dot que se va a llamar AST'''
                self.dot.set_node_default(shape='box')
                self.st = []
                self.id =0

        def __repr__(self):
                return self.dot.to_string()

        def name(self):
                self.id+=1
                return 'n%02d' % self.id

        def generic_visit(self,node):
                #siempre va a pasar poraca cada vez queeste en un nodo
                id = self.name()   
                label = node.__class__.__name__
                NodeVisitor.generic_visit(self,node)
                for field in getattr(node,'_fields'):
                        value=getattr(node,field,None)
                        if isinstance (value,list):
                                for item in value:
                                        self.dot.add_edge(pgv.Edge(id,self.st.pop()))
                        elif isinstance(value,AST):
                                self.dot.add_edge(pgv.Edge(id), self.st.pop())
                        elif value:
                                label += '\\n' + '({}={})'.format(field,value)

                self.dot.add_node(pgv.Node(id,label=label))
                self.st.append(id)



dot = DotVisitor()
print(dot)
