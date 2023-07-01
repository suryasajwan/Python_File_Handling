f=open("hey.txt","r")
data = f.readlines()
print(data)
f.close()

print("\n")
print("#")
f=open("hey.txt","r")
data=f.readlines()
for line in data:
    print(line)

f.close()
print("\n########Without new line#############")

f=open("hey.txt","r")
data2=f.readlines()
for line in data2:
    print(line,end="")


