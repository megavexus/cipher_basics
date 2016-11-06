#!/usr/bin/python
import re
from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1
#AYSY TTYG AHEK YATY ZGEZ YA
#a=4 y b=7
from cipherAbstract import AbstractAfin

class CipherAfin (
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
            if(coprime2(self.key,self.N) !== 1): raise KeyError('The key A must be coprime with N=26')
            if(self.debug): print('Keys: A={1}, B={2}'.format(self.key,self.bkey))
        except ValueError:
            raise KeyError('The key must be an in the form A[,B], beeing A and B integers')
    
    def cipher(self,data):
        for letter in data:
            if(letter.isalpha()):
                if(self.verbose): print("X={} -> C= {} + {}*{}".format(letter,self.key,self.bkey,self.letterOrd(letter)))
                #c = (a + b*x) % N
                numLetter = self.key + self.bkey*self.letterOrd(letter)
                if(numLetter > self.N): numLetter %= self.N
                letter = self.getLetterOrd(letter,numLetter)
            ciphercode += letter
        return ciphercode
     
    def decipher(self,data):
        for letter in data:
            if(letter.isalpha()):
                if(self.verbose): print("X={} -> C= {} + {}*{}".format(letter,self.key,self.bkey,self.letterOrd(letter)))
                #x = (1/a * (c + N - b)) % N
                numLetter = self.key + self.bkey*self.letterOrd(letter)
                if(numLetter > self.N): numLetter %= self.N
                letter = self.getLetterOrd(letter,numLetter)
            ciphercode += letter
        return ciphercode
        
    def letterOrd(self,letter):
        return ord(letter) - ord('A' if letter.isupper() else 'a')
        
    def getLetterOrd(self,letter,num):
        return ord(num) + ord('A' if letter.isupper() else 'a')