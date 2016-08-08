#Importing os Module that help you perform file-processing operations eg Renamiing and Deleting Files
import os

"""The rename() Method"""
#Takes two arguments;the current filename and the new filename
#E.g Renaming a file from test1.txt to test2.txt
os.rename("test1.txt","test2.txt")


"""The remove() Method"""
#Used to delete files by supplying name of the file
#Deleting file test2.txt
os.remove("test2.txt")
