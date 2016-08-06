"""
Create a function that:
	1. Halves even numbers
	2. Doubles odd numbers
	3. Returns the sum of all
"""
"""Pseudo Code"""
#Create a List with integers
#Create a function with a parameter
#Initialize an empty variable
#Create a For loop
#Create an if-Statement to check if:
#If a number is even then its divisible by 2 (num%2 == 0 )
#If divisible then,(num / 2)
#else none
#If a number is odd the its nt divisible by 2 (num%2 != 0)
#if odd then,(num * 2)
#Add the results to an empty variable
#Sum up the results
#Print out Results

"""The Code"""
numbers = [55,66,11,33,44,22,99]

def super_sum(num):
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even = even + (int(i) / 2)
        elif i % 2 != 0:
            odd = odd + (int(i) * 2)
            result = even + odd
    return result
print super_sum(numbers)