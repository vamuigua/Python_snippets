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