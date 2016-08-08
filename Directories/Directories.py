#First imoprt os
import os
###Python Directories###
"""The mkdir() Method"""
#Creating directory "test" in current directory
os.mkdir("test")

"""The chdir() Method"""
#Changing the current directory
#The method takes an argument which is the name of the directory that you want to make the current directory
#os.chdir("new_dir") #NOT SURE

"""The getcwd() Method"""
#Get the Current working directory
os.getcwd()

"""The rmdir() Method"""
#Remove the directory that's passed as the argument
os.rmdir("test")
