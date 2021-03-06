#!/usr/bin/python3
import sys
import argparse
from ciphers.CipherCesar import CipherCesar
from ciphers.CipherRailFence import CipherRailFence
from ciphers.CipherXor import CipherXor
from ciphers.CipherAfin import CipherAfin
from ciphers.CipherPlayfair import CipherPlayfair

#-v|--verbose verboso
#-k FILE -> clave
#-kF -> clave en archivo
#-output filename/path -> Mete output en archivo
#type=cesar|cesar con clave|

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

subparsers = parser.add_subparsers(help='commands', dest='command')
 # create the parser for the "a" command
 # TODO: segun el tipo de cifrado que sea, que de unas subopciones u otras 
 #(por ejemplo, en cesar, meter una palabra aparte del desplazamiento)
parser_encode = subparsers.add_parser('cipher', help='To encode the text')
parser_decode = subparsers.add_parser('decipher', help='To decode the text')

requiredNamed = parser.add_argument_group('Functional named arguments')
requiredNamed.add_argument("-t" ,'--type', help="Code type (ex: Cesar cipher)", type=str, default='cesar', 
    choices=['cesar','railfence','xor','afin', 'playfair'])
requiredNamed.add_argument('-i' ,'--input', help='Input text. If the text contain spaces, it must appear between commas (\'text to encode\')')
requiredNamed.add_argument("-k" ,'--key', help="Code key")
requiredNamed.add_argument("-a" ,'--armor', help="Encode in code64",  action="store_true")

optionalNamed = parser.add_argument_group('Optional named arguments')
#optionalNamed.add_argument('-if','--inputFile', help='Input file name')
optionalNamed.add_argument('-o','--outputFile',help='Output file name. If no present, the output will come in the return')
optionalNamed.add_argument('-kF','--keyFile',help='Code key through file.') #TODO
optionalNamed.add_argument('-iF','--inputFile',help='input text through file.') #TODO

try:

    args = vars(parser.parse_args())
    if(args['verbose']): print(args);
        
    typeCipher = args['type']
    if(typeCipher == 'cesar'):
        cipher = CipherCesar()
    elif(typeCipher == 'railfence'):
        cipher = CipherRailFence()
    elif(typeCipher == 'xor'):
        cipher = CipherXor()    
    elif(typeCipher == 'afin'):
        cipher = CipherAfin()    
    elif(typeCipher == 'f'):
        cipher = CipherPlayfair()
    
    cipher.processParameters(args)
    
    if(args['verbose']):
        cipher.setVerbose()
        
    if(args['command'] == 'decipher'):
        command = 'decipher'
    else:
        command = 'cipher'
    
    key = args['key']
    text = args['input']
    if(key is None): key = str(input("Please enter the code: "))
    cipher.setKey(key.strip())
    if(text is None): text = str(input("Please enter the text to "+command+": "))
    
    
    if(command == 'decipher'):
        code = cipher.decipher(text)
        if(cipher.cipher(code) != text): print('ERROR: NO COINCIDEN: {} -> {} != {}'.format(text,code,cipher.cipher(code)))
    else:
        code = cipher.cipher(text)
        if(cipher.decipher(code) != text): print('ERROR: NO COINCIDEN: {} -> {} != {}'.format(text,code,cipher.decipher(code)))
    
    
    if(args['outputFile'] is not None):
        print(args['outputFile'])
    else:
        print(code)
        
except KeyError as err:
    print ("Key Error: {}".format(err))
