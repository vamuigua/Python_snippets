#Prompt user to input text
#text = raw_input("Please write a word to search for...")

"""print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace"""

#Open files of words.txt
fo = open("learn.txt","r+")
#Write a text in a file
fo.write("Python is a great language.\nYeah its great!!\n");
fo.close()
#reading text in file
fo = open("learn.txt","r+")
mystr = fo.read(10);
print "Read string is:",mystr

#close opened file
fo.close()

#Check the Current Position
fo = open("learn.txt","r+")
position = fo.tell()
print "Current file position is:",position