# ast.py
from sly import Parser
#from genastdot import *
import pydot 
'''
Objetos del AST (Abstract Syntax Tree).

Este archivo define clases para diferentes tipos de nodos de un Árbol 
de sintaxis abstracto. Durante el análisis, creará estos nodos y los 
conectará entre sí. En general, tendrá un nodo AST diferente para cada 
tipo de regla de gramática. Se pueden encontrar algunos nodos AST de 
muestra en la parte superior de este archivo. Tendrá que agregar más 
por su cuenta.
'''

# NO MODIFIQUE
class AST(object):
    _nodes = []
    def __init__(self,*args,**kwargs):
        self.return_type = None
        self.lineno = -1
        self.gen_location= None
        self.hasReturn = None
        
        
        assert len(args) == len(self._nodes)
        for name,value in zip(self._nodes,args):
            setattr(self,name,value)
        if(len(kwargs)!=0):
            for name,value in kwargs.items():
                setattr(self,name,value)
        setattr(self,"_leafDec",False)
        setattr(self,"_leafRed",False)
        setattr(self,"_leafBlue",False)
        setattr(self,"_leaf",False)

    def pprint(self):
        for depth, node in flatten(self):
            print("%s%s" % (" "*(4*depth),node))

    def graphprint(self,name):
        dotty=DotVisitor()
        dotty.visit(self)
        dotty.graph.write_png(name)
        '''dot = DotVisitor()
        print(dot)'''

def validate_fields(**fields):
    def validator(cls):
        old_init = cls.__init__
        def __init__(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            for field,expected_type in fields.items():
                assert isinstance(getattr(self, field), expected_type)
        cls.__init__ = __init__
        return cls
    return validator
    

		
# ----------------------------------------------------------------------
# Nodos espefificos del AST.
#
# Para cada uno de estos nodos, se debe agregar la especificacion
# apropiada de _fields = [] que especifique que campos seran guardados.
# Solo como ejemplo, para el operador binario, se debe guardar el
# operador, la expresion izquierda y la derecha como esto:
#
#    class Expression(AST):
#          pass
#
#    class BinOp(AST):
#          op: str
#          left: Expression
#          right: Expression
#
# En el archivo parser.py, se creara el nodo usando un codigo 
# sililar a esto:
#
#    class PasParser(Parser):
#        ...
#        @_('expr "+" expr')
#        def expr(self, p):
#            return BinOp(p[1], p.expr0, p.expr1)
#
# ----------------------------------------------------------------------

# Nodos Abstract del AST
    


#-------------------------
class program1(AST):
    _nodes = ['identifier','blocks']

class blockk(AST):
    _nodes = ['constant_declaration_part','variable_declaration_part','procedure_declaration_part', 'function_declaration_part','statement_part']

class constantdeclarationpart(AST):
    _nodes = ['constant_definition_list']

class constantdefinitionlist(AST):
    _nodes = ['constants']
    def append(self,e):
        self.constants.append(e)

class constantdefinition(AST):
    _nodes = ['id','constant']

class variabledeclatarionpart(AST):
    _nodes = ['variable_declaration_list']


class variabledeclarationlist(AST):
    _nodes = ['variables']
    def append(self,e):
        self.variables.append(e)

#dfgdfg
class vardeclaration1(AST):
    _nodes = ['identifier','type']
    
class vardeclaration2(AST):
    _nodes = ['identifier_list','type']
    


class identifierlist(AST):
    _nodes = ['identifier']
    def append(self,e):
        self.identifier.append(e)

class typee(AST):
    _nodes = ['type']

class arraytype(AST):
    _nodes = ['index_range','simple_type']

class indexrange(AST):
    _nodes = ['n1','n2']

class simpletype(AST):
    _nodes = ['type_identifier']

class typeidentifier(AST):
    _nodes = ['identifier']
    
#class proceduredeclarationpart(AST):
 #   _nodes = ['procedure_declaration_list']

class proceduredeclarationlist(AST):
    _nodes = ['procedure_declaration_list']
    def append(self,e):
        self.procedure_declaration_list.append(e)

class proceduredeclaration(AST):
    _nodes = ['identifier','block']

class functiondeclarationpart(AST):
    _nodes = ['function_declaration_list']

class functiondeclarationlist(AST):
    _nodes = ['function_declaration_list']
    def append(self,e):
        self.function_declaration_list.append(e)

class functiondeclaration(AST):
    _nodes = ['identifier','formal_parameter','type_identifier','block']

class formalparameter(AST):
    _nodes = ['formal_parameter_list']

class formalparameterlist(AST):
    _nodes = ['formal_parameter_list']
    def append(self,e):
        self.formal_parameter_list.append(e)

class formalparametersection(AST):
    _nodes = ['parameter_group']

class parametergroup(AST):
    _nodes = ['identifier_list','type_identifier']

class statementpart(AST):
    _nodes = ['compound_statement']

class compoundstatement(AST):
    _nodes = ['statement','statement_list']

class statementlist(AST):
    _nodes = ['statement_list']
    def append(self,e):
        self.statement_list.append(e)
        


class statement(AST):
    _nodes = ['statement']

class simplestatement(AST):
    _nodes = ['statement']

class assignamentstatementarray(AST):
    _nodes = ['variable','expression']

class assignamentstatementeter(AST):
    _nodes = ['identifier','expression']

class procedurestatement(AST):
    _nodes = ['procedure_identifier','parameter_list']

class parameterlist(AST):
    _nodes = ['actual_parameter']
    def append(self,e):
        self.actual_parameter.append(e)
        


class actualparameter(AST):
    _nodes = ['actual_parameter']

class procedureidentifier(AST):
    _nodes = ['identifier']
    def append(self,e):
        self.actual_parameter.append(e)

class readstatement(AST):
    _nodes = ['input_variable_list']

class inputvariablelist(AST):
    _nodes = ['input_variable_list']
    def append(self,e):
        self.input_variable_list.append(e)

class inputvariable(AST):
    _nodes = ['variable']

class writestatement(AST):
    _nodes = ['list']

class outputvaluelist(AST):
    _nodes = ['output_value_list']
    def append(self,e):
        self.output_value_list.append(e)

class outputvalue(AST):
    _nodes = ['expression']

class structuredstatement(AST):
    _nodes = ['statement']

class ifstatement(AST):
    _nodes = ['expression','statement1','statement2']

class whilestatement(AST):
    _nodes = ['expression','statement']

class expression(AST):
    _nodes = ['simple1','relational','simple2']

class simpleexpression(AST):
    _nodes = ['sign','term','list']

class addingtermlist(AST):
    _nodes = ['list','op']
    def append(self,term):
        self.list.append(term)

class termm(AST):
    _nodes = ['factor','mult_factor_list']

class multfactorlist(AST):
    _nodes = ['mult_factor_list','op']
    def append(self,factor):
        self.mult_factor_list.append(factor)

class factor(AST):
    _nodes = ['value']

class factorvariable(AST):
    _nodes = ['element']

class factorpar(AST):
    _nodes = ['factor','lpar','rpar']

class factornot(AST):
    _nodes = ['factor','not']

class relationaloperator(AST):
    _nodes = ['op']

class signn(AST):
    _nodes = ['value']

class addingoperator(AST):
    _nodes = ['value']

class multiplyingoperator(AST):
    _nodes = ['value']

class variable(AST):
    _nodes = ['var']

class indexedvariable(AST):
    _nodes = ['var','exp']

class arrayvariable(AST):
    _nodes = ['var']

class variablee(AST):
    _nodes = ['var']

class vids(AST):
    _nodes = ['value']

class ids(AST):
    _nodes = ['value']

class Empty(AST):
    _nodes = []

class BinOp(AST):
    _nodes = ['op','left','right']

class UnyOp(AST):
    _nodes = ['op','value']
	
# ----------------------------------------------------------------------
#                NO MODIFIQUE NADA DE AQUI EN ADELANTE
# ----------------------------------------------------------------------

# Las siguientes clases para visitar y reescribir el AST se toman del 
# módulo ast de Python.
    

# NO MODIFIQUE
class NodeVisitor(object):
    '''
	Clase para visitar los nodos del árbol de análisis sintáctico. 
	Esto se modela después de una clase similar en la biblioteca estándar 
	ast.NodeVisitor. Para cada nodo, el método de visit(node) llama a 
	un método visit_NodeName(node) que debe implementarse en subclases. 
	El método generic_visit() se llama para todos los nodos donde no hay 
	ningún método de matching_NodeName() coincidente.
	
	Este es un ejemplo de un visitante que examina un operador binario:
	
	class VisitOps(NodeVisitor):
	visit_BinOp(self,node):
	print('Binary operator', node.op)
	self.visit(node.left)
	self.visit(node.right)
	visit_UnaryOp(self,node):
	print('Unary operator', node.op)
	self.visit(node.expr)
	
	tree = parse(txt)
	VisitOps().visit(tree)
	'''
    def visit(self,node):
        if node:
            method = 'visit_' + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            return visitor(node)
        else:
            return None

    def generic_visit(self,node):
        for field in getattr(node,"_nodes"):
            value = getattr(node,field,None)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item,AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

# NO MODIFICAR
class NodeTransformer(NodeVisitor):
    def generic_visit(self,node):
        for field in getattr(node,"_nodes"):
            value = getattr(node,field,None)
            if isinstance(value,list):
                newvalues = []
                for item in value:
                    if isinstance(item,AST):
                        newnode = self.visit(item)
                        if newnode is not None:
                            newvalues.append(newnode)
                    else:
                        newvalues.append(n)
                value[:] = newvalues
            elif isinstance(value,AST):
                newnode = self.visit(value)
                if newnode is None:
                    delattr(node,field)
                else:
                    setattr(node,field,newnode)
        return node

# NO MODIFICAR
def flatten(top):
    class Flattener(NodeVisitor):
        def __init__(self):
            self.depth = 0
            self.nodes = []
        def generic_visit(self,node):
            self.nodes.append((self.depth,node))
            self.depth += 1
            NodeVisitor.generic_visit(self,node)
            self.depth -= 1

    d = Flattener()
    d.visit(top)
    return d.nodes



class DotVisitor():
    graph = None
    def __init__(self):
        self.graph = pydot.Dot('AST', graph_type='digraph')
        self.id=0
    def ID(self):
        self.id+=1
        return self.id
        #return "n%d" %self.id

    def visit (self, node):
        if node:
            if(node._leafDec):
                newname = self.visit_leafDec(node)
            elif(node._leafRed):
                newname = self.visit_leafRed(node)
            elif(node._leafBlue):
                newname = self.visit_leafBlue(node)
            elif(node._leaf):
                newname = self.visit_leaf(node)
            else:
                method = 'visit_' + node.__class__.__name__
                visitor = getattr(self, method, self.visit_non_leaf)
                newname= visitor(node)

        self.graph.add_node(newname)
        return newname


    def visit_color(self,node,node_name,node_id,color):
        string= "N%d %s ( %s )" % (self.ID(), node_name, node_id)
        name=pydot.Node(string,shape='box3d', style="filled", fillcolor=color)
        for i in xrange (1,len(node._nodes)):
            if (not isinstance(getattr(node,node._nodes[i]) , list) ):
                newname=self.visit(getattr(node,node._nodes[i]))
                self.graph.add_edge(pydot.Edge(name, newname))
            else:
                for foo in getattr(node,node._nodes[i]):
                    if isinstance(foo,AST):
                        newname = self.visit(foo)
                        self.graph.add_edge(pydot.Edge(name, newname))
        return name



    def visit_non_leaf(self,node):
        string= "N%d %s" % (self.ID(), node.__class__.__name__)
        name=pydot.Node(string,shape='box3d', style="filled", fillcolor="#ffffff")
        for field in getattr(node,"_nodes"):
            value = getattr(node,field,None)
            if isinstance(value,list):
                for item in value:
                    if isinstance(item,AST):
                        newname = self.visit(item)
                        self.graph.add_edge(pydot.Edge(name, newname))


            elif isinstance(value,AST):
                newname = self.visit(value)
                self.graph.add_edge(pydot.Edge(name, newname))
        return name




    def visit_leafBlue(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#0000ff")

    def visit_leafDec(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#9ACD32")

    def visit_leafRed(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#fd0000")

    def visit_leaf(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#ffffff")
                          
