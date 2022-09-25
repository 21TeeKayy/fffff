a = input('Type any word?\n')
i = 0
b = ""
for x in a:
    if a[i].isupper() == True:
        b += a[i].lower()
    elif a[i].islower() == True:
        b += a[i].upper()
    i = i + 1
a = b
print (a)