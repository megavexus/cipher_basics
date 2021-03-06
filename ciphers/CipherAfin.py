#!/usr/bin/python
from cipherAbstract import AbstractCipher
import re
#from math import gcd as bltin_gcd

#def coprime2(a, b):
#    return bltin_gcd(a, b) == 1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1
    
        
def cim(a,m):
    x = 0
    for b in range(m):
        x=((a*b)%m)
        if x == 1:
            return b
    return 0

class CipherAfin (AbstractCipher):
    # 26
    N = 26
    
    def _innerSetKey(self,skey):
        try:
            keys = skey.split(',')
            if(len(keys) == 1):
                self.bkey = 0
            else:
                self.bkey = int(keys[1])%self.N
            self.key = int(keys[0])%self.N
            if(coprime(self.bkey,self.N) != False): raise KeyError('The key A must be coprime with N={}'.format(self.N))
            if(self.verbose): print('Keys: A={0}, B={1}'.format(self.key,self.bkey))
        except ValueError:
            raise KeyError('The key must be an in the form A[,B], beeing A and B integers')
    
    def cipher(self,data):
        ciphercode = ''
        for letter in data:
            if(letter.isalpha()):
                if(self.verbose): print("X={} -> C= {} + {}*{}".format(letter,self.key,self.bkey,self.letterOrd(letter)))
                #c = (b + a*x) % N
                numLetter = (self.bkey + self.key*self.letterOrd(letter)) % self.N
                letter = chr(self.getLetterOrd(letter,numLetter))
            ciphercode += letter
        return ciphercode
     
    def decipher(self,data):
        ciphercode = ''
        ai = cim(self.key,self.N)
        for letter in data:
            if(letter.isalpha()):
                if(self.verbose): print("X={} -> C= {} * ({} + {} - {})".format(letter,ai,self.letterOrd(letter),self.bkey,self.N))
                #x = (1/a * (c + N - b)) % N
                numLetter = int(ai * (self.letterOrd(letter) + self.N - self.bkey)) % self.N
                letter = chr(self.getLetterOrd(letter,numLetter))
            ciphercode += letter
        return ciphercode
        
    def letterOrd(self,letter):
        return ord(letter) - ord('A' if letter.isupper() else 'a')
        
    def getLetterOrd(self,letter,num):
        return num + ord('A' if letter.isupper() else 'a')