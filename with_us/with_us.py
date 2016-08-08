#Using "with" and "us" to automatically close our files
#Open the .txt file and write content using the mode "w" then close the file
with open("text.txt","w") as my_file:

#Write what to be included in the .txt file
    my_file.write("Hello there!")
#Check if file is closed
    if my_file.closed == False:
        my_file.close()
#Print out if file is closed
    print my_file.closed    #Output is: True