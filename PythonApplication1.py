import os
file2 = 'file2'
location = r"C:/Users/Temirlan/Desktop/file"
path = os.path.join(location, file2)
os.mkdir(path)
os.chdir(r"C:/Users/Temirlan/Desktop/file")
os.rename("file2","FILE")
file2 = 'FILE'
path = os.path.join(location, file2)
res = []
for p in os.listdir(location):
    if os.path.isfile(os.path.join(location, p)):
        res.append(p)
print(res)

os.rmdir(path)

