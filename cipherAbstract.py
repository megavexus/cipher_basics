#!/usr/bin/python3

class AbstractCipher:
    'Abstract cipher class'
    key = None
    verbose = False
    preprocess = []
    
    def ___init__(self,skey,isFile=False):
        self.setKey(skey,isFile)
    
    def setVerbose(self):
        self.verbose = True;
    
    def setKey(self,skey,isFile = False):
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
        
    #TODO: Hacer función que extraiga simbolos espaciadores y los guarde en orden (., -)
    """
    def deleteSeparators(self,data):
        for m in re.finditer("[ |,|\.|-|_|]", data):
            for i in range(m.start()-m.end()): setPreprocessItem(data,m.start+i)

        posSpaces = self.find(data,' ')
        data = data.replace(" ", "")
        return 'TODO'
        
    def repairSeparators(self,data):
        return 'TODO'
        
    def setPreprocessItem(self,data,pos):
        self.preprocess.append([data[pos]],pos]
        data[pos] = ' '
    """


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
