#!/usr/bin/python
from cipherAbstract import AbstractCipher
import re, locale
import math


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
        #Normalice the key
        skey = self.preprocessText(skey)
        regex = re.compile('[^a-zA-Z]')
        skey = regex.sub('', skey)
        
        #create the key table
        self.key = []
        for l in skey:
            if l not in self.key:
                letters.remove(l)
                self.key.append(l)
        self.key += letters
        return self.key
        
    def cipher(self,data):
        data = self.preprocessText(data)
        for i in range(len(data)):
        plainData = []
        for letter in data:
            if(letter.isalpha()): plainData.append(letter)

        if(len(plainData)%2 == 1): planData[len(plainData)+1] = 'Q'        
        cipherText = '';
        for i in range(int(len(plainData)/2)):
            #TODO: ord no. Coger funcion que reste ord('A')
            letterA = planData[i]
            letterB = planData[i+1]
            ordA = self.ordLetter(letterA)
            ordB = self.ordLetter(letterB)
            # NO -> Coger la posición en la tabla, no el ord.
            modA = ordA%5
            modB = ordB%5
            divA = int(ordA/5)
            divB = int(ordB/5)
            
            if(modA != modB and divA != divB):
                # SI no coinciden DIVS ni MODS: Coge el DIV1*5+MOD2, DIV2*5+MOD1
            elif(modA != modB and divA == divB):
                # Si coinciden DIVS y ! MODS: Coge el de la izda
            elif(modA == modB and divA != divB):
                # Si coinciden MODS y !DIVS : Coge el de arriba
            elif:
                # Si son iguales: Coge el de la izda.
            
        raise Exception('Not Implemented Yet')

    def decipher(self,data):
        # Igual que cipher, pero al reves.
        raise Exception('Not Implemented Yet')
        
    #transform to uppercase and substitute the I for J
    def preprocessText(self,data):
        data = data.upper()
        return data.replace('I','J')
        
    """
    Returns the letter position in the table
    """
    def ordLetter(self,letter):
        return self.table.index(letter)
        
        