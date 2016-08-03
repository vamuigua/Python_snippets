"""The .isalpha() is used to check if the user_input; a string has characters"""
#Print a Statement
print 'Welcome to the Pig Latin Translator!'

#Prompt the User
original = raw_input('Enter a word:')

#If else statement
if len(original)>0 and original.isalpha():
    print original
else:
    print "empty"
