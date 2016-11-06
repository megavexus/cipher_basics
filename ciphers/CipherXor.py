#!/usr/bin/python
from cipherAbstract import AbstractCipher
import base64

"""
Implements a cipher bit by bit with XOR. It can have the next options:
   -armor: Use an ascii armor.
. Coge el código binarios ASCII del mensaje y de la clave.
. Rellena la clave
"""

class CipherXor (AbstractCipher):
    armor = False
    
    def extraParameters(self,parser):
        parser.add_argument("-a", "--armor", help="codify the output in base64", action="store_true")
    
    def processParameters(self,params):
        if(params['armor'] == True): self.armor = True
    
    def _innerSetKey(self,skey):
        #If is not an integer, throw exception
        try:
            self.key = int(skey.strip())
        except ValueError:
            raise ValueError('Error: The key must be an integer')
        

    """
    Compara mediante XOR el primer array frente al segundo.
    Si son de distinto tamaño, repetirá el de atrás tanto como haga falta
    """
    def _xor(self,data,key):
        rng = len(key)
        # Se invierte

        a = [(1 if (bool(data[i]) != bool(key[i%rng])) else 0) for i in range(len(data))]
        
        if(self.verbose): 
            print('     - DATA:{}'.format(data))
            print('     - KEY:{}'.format(key))
            print('     - XOR:{}'.format(a))
        #return [bool(datab[i]) != bool(keyb[i%rng]) for i in range(len(datab))].reverse()
        return a
        
    def cript(self,data):
        # Parsea a bits los datos y llaves
        dataParse = tobits(data)
        keyParse = numtobits(self.key)

        # Se realiza el XOR
        ciphertext = self._xor(dataParse,keyParse)
        # 
        ciphertext = frombits(ciphertext)
        if(self.verbose): print(' - CIPHERTEXT [{}]: [{}]'.format(data,ciphertext))
        return ciphertext;
        
    def cipher(self,data):
        if(self.verbose): print("+CIPHERING wKey [{}] THE DATA: [{}]".format(self.key,data))
        ciphertext = self.cript(data)
        # Se realiza la armadura ascii si es necesario
        if(self.armor): 
            ciphertext = base64.b64encode(ciphertext.encode('ascii'))
            if(self.verbose): print(' - CIPHERTEXT /W ARMOR [S:{}]: [{}]'.format(len(ciphertext),ciphertext))
        return ciphertext

    def decipher(self,data):
        if(self.verbose): print("+DECIPHERING wKey [{}] THE DATA: [{}]".format(self.key,data))
        if(self.armor): 
            data = str(base64.b64decode(data))
            data = data[2:len(data)-1]
        return self.cript(data)
        
def numtobits(n):
    nbin = bin(int(n))[2:]
    nbin = [int(a) for a in '00000000'[len(nbin):] + nbin]
    return nbin

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


