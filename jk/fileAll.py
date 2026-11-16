file = open("myFile.txt","w")
file.write("Good morning!!!")
file.close()

file = open("myFile.txt","a")
file.write("Good evening!!!")
file.close()

file = open("myFile.txt","r")
lines = file.read()
print(lines)
file.close()