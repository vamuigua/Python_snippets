#Open details.txt file and write in it using the mode "w"
my_file = open("details.txt", "w")

#Write data in the .txt file
my_file.write("I'm the first line of the file!" + "\n")
my_file.write("I'm the second line." + "\n")
my_file.write("Third line here, boss." + "\n")

#Close the .txt file
my_file.close()

#Open the .txt file
my_file = open("details.txt","r")
#Read the content line by line while printing it out
print my_file.readline()
print my_file.readline()
print my_file.readline()

#Close the .txt file
my_file.close()

#Reading only the first 10 characters(Including the spaces)
my_file = open("details.txt","r+")
reading = my_file.read(10)
print "Read string is: ",reading

#Read the Current File Position
position = my_file.tell()
print "The current position is: ",position

#Reading the next 9 characters
reading2 = my_file.read(5)
print "Read string is: ",reading2
#Reading the current file position after reading the next 9 characters
position = my_file.tell()
print "The current position is: ",position

#Close the File
my_file.close()



