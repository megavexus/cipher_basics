#!/usr/bin/python
import re
from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1
#AYSY TTYG AHEK YATY ZGEZ YA
#a=4 y b=7
    def _innerSetKey(self,skey):

class CipherAfin (
    N = 26
    
    def _innerSetKey(self,skey):
        try:
            keys = skey.split(',')
            if(len(keys) == 1):
                self.bkey = 0
            else:
                
                self.bkey = int(keys[1])%self.N
                
            self.key = int(keys[0])%self.N
            if(coprime2(self.key,self.N) !== 1): raise KeyError('The key A must be coprime with N=26')
            if(self.debug): print('Keys: A={')
        except ValueError:
            raise KeyError('The key must be an in the form A[,B], beeing A and B integers')
    
    def cipher(self,data):
        #quita espacios y puntuaciones
        #c = (a + xb) % N
        
        #devuelve espacios y puntuaciones
        return False
     
    def decipher(self,data):
        #x = (1/a * (c + N - b)) % N
        return False