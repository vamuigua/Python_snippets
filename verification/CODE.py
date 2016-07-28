#Prompt window to write your name
name = raw_input("Please write your name...")
#Open file of names.txt
openfile = open("names.txt", "r+")
#Check if name is in file
if name not in openfile.readline():
#write name in file if note found
    openfile.write(name)
#file closes
    openfile.close()
    print ("Success!")
#Else statement to print if false
else:
    print ('Name not found')
    openfile.close()