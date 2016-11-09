#!/usr/bin/python
from cipherAbstract import AbstractCipher
import re, locale


class CipherPlayfair (AbstractCipher):
    """
    Cipher and decipher with the playfair cipher. 
    -- http://making-code.blogspot.com.es/2015/07/cifrado-de-playfair.html
    Imputs:
        -k: A text to make the playfair matrix
        -i: texto to cipher/decipher
    the output will be in uppercase (or no?)
    """
    def _innerSetKey(self,skey):
        #extract I of the table
        letters = [chr(i + ord('A')) for i in range(26) ]
        letters.remove('I')
        print(letters)
        #Normalice the key
        print(skey)
        skey = self.preprocessText(skey)
        regex = re.compile('[^a-zA-Z]')
        skey = regex.sub('', skey)
        
        print(skey)
        #create the key table
        self.key = []
        for l in skey:
            if l not in self.key:
                letters.remove(l)
                self.key.append(l)
        self.key += letters
        print(self.key)
        raise Exception('Not Implemented Yet')
        
    def cipher(self,data):
        raise Exception('Not Implemented Yet')

    def decipher(self,data):
        raise Exception('Not Implemented Yet')
        
    #transform to uppercase and substitute the I for J
    def preprocessText(self,data):
        data = data.upper()
        return data.replace('I','J')
        