f1=open("copy1.txt","r")
f2=open("copy2.txt","w")

data=f1.readlines()
print(data)

for line in data:
    f2.write(line)

f1.close()
f2.close()
