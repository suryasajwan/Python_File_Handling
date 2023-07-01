f=open("hello.txt","r")
data=f.read()
print(data)
f.close()


f=open("hello.txt","r")
data=f.read(10)
print(data)
print(f.read(4))
