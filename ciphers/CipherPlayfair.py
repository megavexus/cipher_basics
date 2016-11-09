#!/usr/bin/python
from cipherAbstract import AbstractCipher

#http://making-code.blogspot.com.es/2015/07/cifrado-de-playfair.html

class CipherPlayfair (AbstractCipher):

    def _innerSetKey(self,skey):
        raise Exception('Not Implemented Yet')
        
    def cipher(self,data):
        raise Exception('Not Implemented Yet')

    def decipher(self,data):
        raise Exception('Not Implemented Yet')
