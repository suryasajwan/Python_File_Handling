f=open("hey.txt","r")

print(f.tell())
f.seek(10)
print(f.tell())
print(f.read())
