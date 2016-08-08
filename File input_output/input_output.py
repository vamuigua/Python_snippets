# Generates a list of squares of the numbers 1 - 10
my_list = [i**2 for i in range(1,11)]

#Opening a file(output.txt) with mode of "write"
f = open("output.txt", "r+")

#For loop to loop through my_list
for item in my_list:
    #Write the numbers in my_list to output.txt
    f.write(str(item) + "\n")

#If statetement to check if the .txt file is closed
#If not closed, close the file
if f.closed == False:
    f.close()
#Print tio check its closed
    print f.closed