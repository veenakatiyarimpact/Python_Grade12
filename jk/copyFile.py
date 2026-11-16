file = open("pune.txt","r")
txt = file.read()
file.close()

file = open("pune1.txt" , "w")
file.write(txt)
file.close()
