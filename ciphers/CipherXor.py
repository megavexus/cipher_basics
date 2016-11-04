#!/usr/bin/python

from cipherAbstract import AbstractCipher

"""
Implements a cipher bit by bit with XOR. It can have the next options:
   -armor: Use an ascii armor.
   -das
"""

class CipherXor (AbstractCipher):
    armor = False
    
    def extraParameters(self,params):
        return False
    
    def processParameters(self,params):
        return False
    
    def _innerSetKey(self,skey):
       self.key = int(skey.strip())
       