f=open("hey.txt","r")

Lines=0
Words=0
Chars=0

for line in f:
    Lines+=1
    line=line.strip("\n")
    Chars+=len(line)
    list1=line.split()
    Words+=len(list1)
f.close()
print("word:",Words)
print("line:",Lines)
print("char:",Chars)