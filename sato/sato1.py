""""Create a function that gets the sum of all the digits in a list given as a parameter"""""
""""Pseudo code"""""
#Make a list with intergers/digits
#Create a Function with a parameter
#Create an temporary empty variable to store the sum of the digits
#Create a for-loop to loop through the entire list
#Store the total value in our empty variable that we created
#Return the result/Total
#Call the Function to execute the code in the function by printing it

""""The Code"""
# List of Numbers
numbers = [12,23,34,56,78,98,56,83]

#Defining a Function called addition with hut as parameter
def addition(hut):
    # Temporary empty variable
    total = 0
    # For-loop-For every digit in hut
    for i in hut:
        # For-loop-For every digit in number
        for u in str(i):
            # Add the total of the numbers to total
            total = int(u) + total
    # Return the result
    return total
#Print the result of calling the function
print addition(numbers)