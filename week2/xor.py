import binascii
import sys
from string import Formatter

print "Comparing "+sys.argv[1]+" with "+sys.argv[2]

def c2b(hex_str):
  bin_str = ""
  for c in binascii.unhexlify(hex_str):
    trunc = bin(ord(c))[2:]
    bin_str += '{:0>8}'.format(trunc)
  return bin_str

def compare(bin_str_1, bin_str_2):
  for i in range(0, len(bin_str_1)):
    if bin_str_1[i] == bin_str_2[i]:
      return False
  return True

print c2b(sys.argv[1])
print c2b(sys.argv[2])

if compare(c2b(sys.argv[1]),c2b(sys.argv[2])):
  print "They are xors of each other.";
else:
  print "They are not xors of each other.";
