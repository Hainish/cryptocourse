import sys

z = int(sys.argv[1])
g = int(sys.argv[2])

for x in range(1,z):
  print x
  if g**x % z == 1:
    break
