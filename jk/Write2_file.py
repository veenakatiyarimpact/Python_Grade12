file = open("apple.txt","w")

file.write("This is mango")
file.close()

v=open("apple.txt","r").read()
print(v)

if v== "This is apple":
    print("Yes it is apple")

else :
    print("no it is not apple")