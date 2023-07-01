import os

f=open("hello.txt","r")

if os.path.isfile("hello.txt"):
    print(" file exist")

else:
  print("not exist")


print(os.path.isfile("hello.txt"))



