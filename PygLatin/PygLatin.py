#String "ay" to be added at the end
pyg = 'ay'

#Prompting for User input
original = raw_input('Enter a word:')

#If else condition
#".isalpha()" used to chech if string has characters only
if len(original) > 0 and original.isalpha():
#To lower case the word
    word = original.lower()
#To take the first character in the word
    first = word[0]
#To print the new-word fully
    new_word = word + first + pyg
#To begin new_word from first index
    new_word = new_word[1:len(new_word)]
#Print the original word
    print original
else:
#Return statement if False
    print 'empty'
