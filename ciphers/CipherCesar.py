#!/usr/bin/python

from cipherAbstract import AbstractCipher

class CipherCesar (AbstractCipher):
    def _innerSetKey(self,skey):
       self.key = int(skey.strip())
       
    def cipher(self,data):
        ciphercode = ""
        for letter in data:
            if(letter.isalpha()):
                numLetter = ord(letter) + self.key 
                if numLetter > ord('Z' if letter.isupper() else 'z'):
                    numLetter -= 26
                letter = chr(numLetter)
            ciphercode += letter
        print (ciphercode)
        return ciphercode
     
    def decipher(self,data):
        plaintext = ''
        for letter in data:
            if(letter.isalpha()):
                numLetter = ord(letter) - self.key 
                if numLetter > ord('Z' if letter.isupper() else 'z'):
                    numLetter -= 26
                letter = chr(numLetter)
            plaintext = plaintext + letter
        return plaintext