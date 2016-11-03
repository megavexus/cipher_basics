#!/usr/bin/python3
import sys
import argparse
from ciphers.CipherCesar import CipherCesar

#parametros por defecto: cifrado.
    #http://stackoverflow.com/questions/9505898/conditional-command-line-arguments-in-python-using-argparse
    #https://docs.python.org/3/howto/argparse.html
    #http://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/

#-v|--verbose verboso
#-k -> clave
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
requiredNamed.add_argument("-t" ,'--type', help="Code type (ex: Cesar cipher)", type=str, default='cesar', choices=['cesar'])
requiredNamed.add_argument('-i' ,'--input', help='Input text. If the text contain spaces, it must appear between commas (\'text to encode\')')
requiredNamed.add_argument("-k" ,'--key', help="Code key")

optionalNamed = parser.add_argument_group('Optional named arguments')
#optionalNamed.add_argument('-if','--inputFile', help='Input file name')
optionalNamed.add_argument('-o','--outputFile',help='Output file name. If no present, the output will come in the return')


args = vars(parser.parse_args())
print(args);

typeCipher = args['type']
if(typeCipher == 'cesar'):
    cipher = CipherCesar()
    
if(args['command'] == 'decipher'):
    command = 'decipher'
else:
    command = 'cipher'

key = args['key']
text = args['input']
if(key is None): key = str(input("Please enter the code: "))
cipher.setKey(key.strip())
if(text is None): text = str(input("Please enter the text to "+command+": "))

print(command+' the text '+text+' under the key '+key)
if(command == 'decipher'):
    code = cipher.decipher(text)
else:
    code = cipher.cipher(text)



