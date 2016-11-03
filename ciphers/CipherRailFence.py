#!/usr/bin/python

from cipherAbstract import AbstractCipher

class CipherRailFence (AbstractCipher):
    def _innerSetKey(self,skey):
       self.key = int(skey.strip())
       
    def find(self,s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]
       
    def fence(self, lst, numrails):
        varFence = [[None] * len(lst) for n in range(numrails)]
        rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
        for n, x in enumerate(lst):
            varFence[rails[n % len(rails)]][n] = x
    
        return [c for rail in varFence for c in rail if c is not None]
    
    def cipher(self,data):
        cipherWord = self.fence(data.replace(" ", ""), self.key)
        posSpaces = self.find(data,' ')
        for i in posSpaces: cipherWord = cipherWord[:i] + [' '] + cipherWord[i:]
        return ''.join(cipherWord);
     
    def decipher(self,data):
        posSpaces = self.find(data,' ')
        data = data.replace(" ", "")

        rng = range(len(data))
        pos = self.fence(rng, self.key)
        plain = [data[pos.index(self.key)] for self.key in rng]
        for i in posSpaces: plain = plain[:i] + [' '] + plain[i:]
        return ''.join(plain)
        
    

    


