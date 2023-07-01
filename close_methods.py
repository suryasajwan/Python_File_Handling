###########  normal way ############333
print("\n Normal way......")
f=open("hello.txt","w+")
print(f.readable())

f.close()

#############   By try final method ####################
print("\nThrough try and final method ..........")
try:
 f=open("hello.txt","w+")
 print(f.writable())

finally:
    f.close()


####################  with statement  #################
print("\n Through with statement..... ")
with open("hello.txt","w+") as f:
    print("File name is :-",f.name)
    print("Mode of file is:-",f.mode)
    print("\n")
    data=f.read()
    print(data)

