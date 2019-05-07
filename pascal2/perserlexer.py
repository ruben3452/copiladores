
from sly import Parser
from lexer2 import pascal1
from ast import *






class PasParser(Parser):
    tokens = pascal1.tokens
    literals = pascal1.literals
    
    precedence = (
       ('left', 'AND', 'NOT', 'OR'),
       ('left', 'DIV' ),
      
       ('left', '+', '-'),
       ('right', 'ELSE'),
       )
    
    start = 'program'
    
    _leafRed = False
    _leafDec = False
    _leafBlue = False
   
        	
    @_('PROGRAM identifier SEMICOLON block PERIOD')
    def program(self,p):
        return program1(p.identifier,p.block)

    @_('constant_declaration_part variable_declaration_part procedure_declaration_part function_declaration_part statement_part')
    def block(self,p):
        return blockk(p.constant_declaration_part, p.variable_declaration_part, p.procedure_declaration_part, p.function_declaration_part, p.statement_part)

    @_('empty')
    def constant_declaration_part(self,p):
        return constantdeclarationpart([])

    @_('CONSTAN constant_definition_list')
    def constant_declaration_part(self,p):
        return constantdeclarationpart(p.constant_definition_list)

    @_('constant_definition SEMICOLON')
    def constant_definition_list(self,p):
        return constantdefinitionlist([p.constant_definition])

    @_('constant_definition SEMICOLON constant_definition_list')
    def constant_definition_list(self,p):
        p.constant_definition_list.append(p[0])
        return constantdefinitionlist(p.constant_definition_list)

    @_('identifier ASSIGN NUMBER')
    def constant_definition(self,p):
        return constantdefinition(p.identifier,p[2])

    @_('identifier ASSIGN CHART')
    def constant_definition(self,p):
        return constantdefinition(p.identifier,p[2])

    @_('identifier ASSIGN identifier')
    def constant_definition(self,p):
        return constantdefinition(p[0],p[2])

    @_('empty')
    def variable_declaration_part(self,p):
        return Empty()

    @_('VAR variable_declaration_list' )
    def variable_declaration_part(self,p):
        return variabledeclatarionpart(p.variable_declaration_list)

    @_('var_declaration SEMICOLON')
    def variable_declaration_list(self,p):
        return variabledeclarationlist([p.var_declaration])
    
    @_('var_declaration COMA variable_declaration_list')
    def variable_declaration_list(self,p):
        p.variable_declaration_list.append(p.var_declaration)
        return variabledeclarationlist(p.variable_declaration_list)
    

    @_('identifier COMA identifier COLON type')
    def var_declaration(self,p):
        self._leafDec = True
        return vardeclaration1(p.identifier,p.type)

    @_('identifier_list COLON type')
    def var_declaration(self,p):
        return vardeclaration2(p.identifier_list,p.type)
    
    
    @_('identifier')
    def identifier_list(self,p):
        return identifierlist([p.identifier])

    @_('identifier COMA identifier_list')
    def identifier_list(self,p):
        p.identifier_list.append(p.identifier)
        return identifierlist(p.identifier_list)

    @_('simple_type')
    def type(self,p):
        return typee(p.simple_type)

    @_('array_type')
    def type(self,p):
        return typee(p.array_type)

    @_('ARRAY LCORCHET index_range RCORCHET OF simple_type')
    def array_type(self,p):
        return arraytype(p.index_range,p.simple_type)

    @_('NUMBER PERIODOUBL NUMBER')
    def index_range(self,p):
        return indexrange(p[0],p[2])

    @_('type_identifier')
    def simple_type(self,p):
        return simpletype(p.type_identifier)

    @_('identifier')
    def type_identifier(self,p):
        return typeidentifier(p.identifier)

    @_('procedure_declaration_list')
    def procedure_declaration_part(self,p):
        return proceduredeclarationlist(p.procedure_declaration_list)
    
    

    @_('empty')
    def procedure_declaration_list(self,p):
        return proceduredeclarationlist([])

    @_('procedure_declaration SEMICOLON')
    def procedure_declaration_list(self,p):
        return proceduredeclarationlist([p.procedure_declaration])

    @_('procedure_declaration_list procedure_declaration SEMICOLON')
    def procedure_declaration_list(self,p):
        p.procedure_declaration_list.append(p.procedure_declaration)
        return proceduredeclarationlist(p.procedure_declaration_list)

    @_('PROCEDURE ID SEMICOLON block')
    def procedure_declaration(self,p):
        return proceduredeclaration(p[1],p.block)

    @_('function_declaration_list')
    def function_declaration_part(self,p):
        return functiondeclarationpart(p.function_declaration_list)

    @_('empty')
    def function_declaration_list(self,p):
        return functiondeclarationlist([])

    @_('function_declaration SEMICOLON')
    def function_declaration_list(self,p):
        return functiondeclarationlist([p.function_declaration])

    @_('function_declaration_list function_declaration SEMICOLON')
    def function_declaration_list(self,p):
        p.function_declaration_list.append(p.function_declaration)
        return functiondeclarationlist(p.function_declaration_list)

    @_('FUNCTION identifier formal_parameter COLON type_identifier SEMICOLON block')
    def function_declaration(self,p):
        return functiondeclaration(p.identifier,p.formal_parameter,p.type_identifier,p.block)
    
    

    @_('LPAREN formal_parameter_list RPAREN')
    def formal_parameter(self,p):
        return formalparameter(p.formal_parameter_list)

    @_('formal_parameter_section')
    def formal_parameter_list(self,p):
        return formalparameterlist([p.formal_parameter_section])

    @_('formal_parameter_list SEMICOLON formal_parameter_section')
    def formal_parameter_list(self,p):
        p.formal_parameter_list.append(p.formal_parameter_section)
        return formalparameterlist(p.formal_parameter_list)

    @_('parameter_group')
    def formal_parameter_section(self,p):
        return formalparametersection(p.parameter_group)

    @_('VAR parameter_group')
    def formal_parameter_section(self,p):
        return formalparametersection(p.parameter_group)

    @_('FUNCTION parameter_group')
    def formal_parameter_section(self,p):
        return formalparametersection(p.parameter_group)

    @_('PROCEDURE parameter_group')
    def formal_parameter_section(self,p):
        return formalparametersection(p.parameter_group)

    @_('identifier_list COLON type_identifier')
    def parameter_group(self,p):
        return parametergroup(p.identifier_list,p.type_identifier)


    @_('compound_statement')
    def statement_part(self,p):
        return statementpart(p.compound_statement)

    
    
    @_('BEGIN statement statement_list END ')
    def compound_statement(self,p):
        return compoundstatement(p.statement,p.statement_list)
    
   

    @_('SEMICOLON statement statement_list')
    def statement_list(self,p):
        p.statement_list.append(p.statement)
        return statementlist(p.statement_list)

    @_('empty')
    def statement_list(self,p):
        return statementlist([])
    


    @_('simple_statement')
    def statement(self,p):
        return statement(p.simple_statement)

    @_('structured_statement')
    def statement(self,p):
        return statement(p.structured_statement)

    @_('assignament_statement_eter')
    def simple_statement(self,p):
        return simplestatement(p.assignament_statement_eter)

    @_('assignament_statement_array')
    def simple_statement(self,p):
        return simplestatement(p.assignament_statement_array)

    @_('procedure_statement')
    def simple_statement(self,p):
        return simplestatement(p.procedure_statement)

    @_('read_statement')
    def simple_statement(self,p):
        return simplestatement(p.read_statement)

    @_('write_statement')
    def simple_statement(self,p):
        return simplestatement(p.write_statement)

    @_('identifier BECOMES expression')
    def assignament_statement_eter(self,p):
        self._leafBlue = True
        return assignamentstatementeter(p.identifier,p.expression)

    @_('indexed_variable ASSIGN expression')
    def assignament_statement_array(self,p):
        return AssignamentStatementArray(p.indexed_variable,p.expression)

    @_('procedure_identifier LPAREN parameter_list RPAREN')
    def procedure_statement(self,p):
        return procedurestatement(p.procedure_identifier,p.parameter_list)

    @_('procedure_identifier')
    def procedure_statement(self,p):
        return procedurestatement(p.procedure_identifier,[])

    @_('actual_parameter')
    def parameter_list(self,p):
        return parameterlist([p.actual_parameter])

    @_('parameter_list COMA actual_parameter')
    def parameter_list(self,p):
        p.parameter_list.append(p.actual_parameter)
        return parameterlist(p.parameter_list)

    @_('expression')
    def actual_parameter(self,p):
        return actualparameter([p.expression])


    @_('actual_parameter COLON expression')
    def actual_parameter(self,p):
        p.actual_parameter.append(p.expression)
        return actualparameter(p.actual_parameter)
    
   
    @_('identifier')
    def procedure_identifier(self,p):
        return procedureidentifier(p.identifier)

    @_('READ LPAREN input_variable_list RPAREN')
    def read_statement(self,p):
        return readstatement(p.input_variable_list)

    @_('input_variable')
    def input_variable_list(self,p):
        return inputvariablelist([p.input_variable])

    @_('input_variable_list COMA input_variable')
    def input_variable_list(self,p):
        p.input_variable_list.append(p.input_variable)
        return inputvariablelist(p.input_variable)

    @_('variable')
    def input_variable(self,p):
        return inputvariable(p.variable)

    @_('WRITE LPAREN output_value_list RPAREN')
    def write_statement(self,p):
        return writestatement(p.output_value_list)

    @_('output_value')
    def output_value_list(self,p):
        return outputvaluelist([p.output_value])

    @_('output_value_list COMA output_value')
    def output_value_list(self,p):
        p.output_value_list.append(p.output_value)
        return outputvaluelist(p.output_value_list)

    @_('expression')
    def output_value(self,p):
        return outputvalue(p.expression)

    @_('compound_statement')
    def structured_statement(self,p):
        return structuredstatement(p.compound_statement)

    @_('if_statement')
    def structured_statement(self,p):
        return structuredstatement(p.if_statement)

    @_('while_statement')
    def structured_statement(self,p):
        return structuredstatement(p.while_statement)

    @_('IF expression THEN statement')
    def if_statement(self,p):
        return ifstatement(p.expression,p.statement,None)

    @_('IF expression THEN statement ELSE statement')
    def if_statement(self,p):
        return ifstatement(p.expression,p.statement0,p.statement1)

    @_('WHILE expression DO statement')
    def while_statement(self,p):
        return whilestatement(p.expression,p.statement)

    @_('simple_expression')
    def expression(self,p):
        return expression(p.simple_expression,None,None)

    @_('simple_expression relational_operator simple_expression')
    def expression(self,p):
        return expression(p.simple_expression0,p.relational_operator,p.simple_expression1)

    @_('sign term adding_term_list')
    def simple_expression(self,p):
        return simpleexpression(p.sign,p.term,p.adding_term_list)

    @_('empty')
    def adding_term_list(self,p):
        return addingtermlist([],None)

    @_('adding_term_list adding_operator term')
    def adding_term_list(self,p):
        return BinOp(p.adding_operator,p.adding_term_list,p.term)

    @_('factor mult_factor_list')
    def term(self,p):
        return termm(p.factor,p.mult_factor_list)

    @_('empty')
    def mult_factor_list(self,p):
        return multfactorlist([],None)

    @_('mult_factor_list multiplying_operator factor')
    def mult_factor_list(self,p):
        p.mult_factor_list.append(p.factor)
        return multfactorlist(p.mult_factor_list,p.multiplying_operator)

    @_('variable')
    def factor(self,p):
        return factorvariable(p[0])

    @_('NUMBER')
    def factor(self,p):
        return factor(p[0],_leaf = True)

    @_('CHART')
    def factor(self,p):
        return factor(p[0],_leaf = True)

    @_('LPAREN expression RPAREN')
    def factor(self,p):
        return factorpar(p[1],p[0],p[2])

    @_('NOT factor')
    def factor(self,p):
        return factornot(p[1],p[0])

    @_('procedure_statement')
    def factor(self,p):
        return factor(p.procedure_statement)

    @_('ASSIGN')
    def relational_operator(self,p):
        return relationaloperator(p)

    @_('NOTEQUAL')
    def relational_operator(self,p):
        return relationaloperator(p)

    @_('MENOR')
    def relational_operator(self,p):
        return relationaloperator(p)

    @_('MENORIGUAL')
    def relational_operator(self,p):
        return relationaloperator(p)

    @_('MAYORIGUAL')
    def relational_operator(self,p):
        return relationalOperator(p)

    @_('MAYOR')
    def relational_operator(self,p):
        return relationalOperator(p)

    @_("'+'")
    def sign(self,p):
        return signn(p[0])

    @_("'-'")
    def sign(self,p):
        return signn(p[0])

    @_('empty')
    def sign(self,p):
        return signn(None)

    @_("'+'")
    def adding_operator(self,p):
        return addingoperator(p[0],_leaf = True)

    @_("'-'")
    def adding_operator(self,p):
        return addingoperator(p[0],_leaf = True)

    @_('OR')
    def adding_operator(self,p):
        return addingoperator(p[0],_leaf = True)

    @_("'*'")
    def multiplying_operator(self,p):
        return multiplyingoperator(p[0],_leaf = True)

    @_("'/'")
    def multiplying_operator(self,p):
        return multiplyingoperator(p[0],_leaf = True)
    
    @_('DIV')
    def multiplying_operator(self,p):
        return multiplyingoperator(p[0],_leaf = True)

    @_('AND')
    def multiplying_operator(self,p):
        return multiplyingoperator(p[0],_leaf = True)

    @_('entire_variable')
    def variable(self,p):
        return variablee(p.entire_variable)

    @_('indexed_variable')
    def variable(self,p):
        return variablee(p.indexed_variable)

    @_('array_variable LCORCHET expression RCORCHET')
    def indexed_variable(self,p):
        return indexedvariable(p.array_variable,p.expression)

    @_('entire_variable')
    def array_variable(self,p):
        return arrayvariable(p.entire_variable)

    @_('variable_identifier')
    def entire_variable(self,p):
        self._leafRed = True
        return variablee(p.variable_identifier)

    @_('ID')
    def variable_identifier(self,p):
        line = p.lineno
        index = p.index
        return vids(p[0],_leaf = True)

    @_('ID')
    def identifier(self,p):
        line = p.lineno
        index = p.index
        return ids(p[0],_leaf = True)

    @_('')
    def empty(self,p):
        return Empty()   
    

    
    
