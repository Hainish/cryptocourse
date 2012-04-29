import binascii,sys
from string import Formatter

def build_xor():
  xor_string = ''
  for x,y in zip(binascii.unhexlify(sys.argv[1]), binascii.unhexlify(sys.argv[2])):
    trunc = hex(ord(x) ^ ord(y))[2:]
    xor_string += '{:0>2}'.format(trunc)
  print xor_string

build_xor()
