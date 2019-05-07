
from sly import Lexer



class pascal1(Lexer):

    keywords = { 'program', 'var', 'array', 'of', 'procedure', 
               'begin', 'end', 'read', 'write', 'if', 'then', 
               'else', 'while', 'do', 'not', 'constan',
               'or', 'div', 'and', 'function'
               }
    
    tokens = { ID, NUMBER,
            LPAREN, RPAREN, LCORCHET, RCORCHET, MENOR,
            MENORIGUAL,MAYOR, MAYORIGUAL, NOTEQUAL, ASSIGN, 
            BECOMES, PERIOD, COLON, SEMICOLON, PERIODOUBL,
            COMA,CHART,*{kw.upper() for kw in keywords}
            
            #reservadas
           
            
            
            }
         
            
    
    
    literals = { '+','-','*','/','true','false','boolean' }
    


    # String containing ignored characters
    ignore = ' \t'
  
    
   

    ignore_commentt = r'\(\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*?\*+\)|{[^{]*}'
 
    
    # Regular expression rules for tokens

    

    
    
    #singnos comparaciones
    
    
    CHART = r'\'[^\']*\'|"[^"]*"'
    ASSIGN  = r'='
    MENORIGUAL   = r'<'+ASSIGN
    MAYORIGUAL = r'>'+ASSIGN
    MAYOR = r'>'
    MENOR   = r'<'
    NOTEQUAL = r'\<>'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LCORCHET = r'\['
    RCORCHET = r'\]'
    BECOMES = r'\:='
    PERIOD = r'\.'
    COMA = r'\,'
    PERIODOUBL = r'\.'+PERIOD
    COLON = r'\:'
    SEMICOLON = r'\;'
    
   

    
    
    
    @_(r'[a-zA-z][a-zA-Z0-9]*')
    def ID(self,t):
        if t.value.lower() in self.keywords:
            t.type = t.value.upper()
        return t
    
    @_(r'[0-9]+')
    def NUMBER(self,t):
        t.value = int(t.value)
        return t
  
    
   
    
    
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
        
    def error(self,t):
        print("Line %d: Illegal character '%s'" % (self.lineno,t.value[0]))
        self.index += 1
        


def printLex(file,lexer):
    opent = open(file)
    archi = opent.read()
    print("\t\t\tPROGRAM: %r\n\n" % (file))
    print("LEXER RESULTS:")
    for tok in lexer.tokenize(archi):
        print('type=%r, value=%r' % (tok.type, tok.value))

