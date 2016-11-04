#!/usr/bin/python3

class AbstractCipher:
    'Abstract cipher class'
    def ___init__(self,skey,isFile=False):
        self.setKey(skey,isFile)
    
    def setKey(self,skey,isFile = False):
        print(skey);
        if(isFile):
            # Intenta obtener el archivo. Si no, error.
            self._innerSetKey(file_get_contents(skey))
        else:
            self._innerSetKey(skey)
            
        if (self.key is None): return False
    
    def _innerSetKey(self,skey):
       self.key = skey.strip()
       
    def cipher(self,data):
     print ("FUNCTION NOT DEFINED")
     
    def decipher(self,data):
        print ("FUNCTION NOT DEFINED")
     
    ##TODO: Pide parámetros extra.
    def extraParameters(self,params):
        return False
        
    ##TODO
    def processParameters(self,params):
        return False


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
