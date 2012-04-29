import sys, fractions

z = int(sys.argv[1])

x=0
print 'relatively prime: ',
for y in range(1,z):
  if fractions.gcd(y,z) == 1:
    print str(y)+',',
    x+=1

print '\nsize of group '+str(z)+' = '+str(x)
