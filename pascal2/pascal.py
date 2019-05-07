#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lexer2 import *
from perserlexer import *
from ast import *
import sys
import os


    
if __name__ == '__main__':
 
                
            file = "test1.txt"
            lexer = pascal1()
            
            if len(sys.argv) > 1:
                
                files = sys.argv[2:len(sys.argv)]
               
                if sys.argv[1] == "-1" or sys.argv[1] == "-2":
                    
                    for f in files:
                        if os.path.isfile(f):
                            printLex(f,lexer)
                        else:
                            print("ERROR: el archivo %r no existe" % f)
                            print("-------------------------------------\n")
            
                elif sys.argv[1] == "-3":
                    
                    for f in files:
                        
                        if os.path.isfile(f):
                            
                            lexer = pascal1()
                            parser = PasParser()
                            opent = open(f)
                            archi = opent.read()
                            resultx = parser.parse(lexer.tokenize(archi))
                            
                            fSplit = f.split('/')
                            fPas = fSplit[-1]
                            fPasSplit = fPas.split('.')
                            nameFile = fPasSplit[0]
                            pathJPG = "ast/" + nameFile + ".png"
                            
                            if resultx:
                                print("\n\nParser esta completo. guardado en la carpeta AST:")
                                print(pathJPG)
                                resultx.graphprint(pathJPG)
                                
                        else:
                            print("ERROR: el archivo %r no existe" % f)           
                            

                 
                 
                 

