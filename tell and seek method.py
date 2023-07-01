print("####### tell and seek method #########")

f = open("hey.txt","r")
print(f.tell())  # initial cursor position =0

print(f.read(4))
print(f.tell())
print(f.read())
print(f.tell())

f.close()

print("\n#########  Seek method ###########")
f=open("hey.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.seek(0))
print(f.read(4))
