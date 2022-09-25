import sys

print ("List is: ",sys.argv[0])
n = len(sys.argv[1])
a = sys.argv[1][0:1]
#print (a)
if a == '[':
    print ('List')
a = sys.argv[1][0:n]
for x in a:
    if x.isupper() == True:
        print ("String")
        sys.exit()
    if x.islower() == True:
        print ("String")
print ("Int")