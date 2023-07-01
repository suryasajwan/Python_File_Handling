f=open("w+.txt","w+")
f.write("bye bye")

f.seek(0)
data=f.read()
print(data) 
f.close()