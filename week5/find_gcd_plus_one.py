import sys
a = 0
z = int(sys.argv[1])
n = int(sys.argv[2])
while True:
  a += 1
  print 'a:',
  print a
  am = n * a
  if am % z == 1:
    break

b = (am - 1) / z
print 'b: '+str(b)
