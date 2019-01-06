print("Hello World")
#use a comma to separate different data types in single print statement
print("5 + 2 =", 5 + 2)
#use backslash to escape quotation marks
quote = "\"Always remember you are unique\""
#use three single quotation marks to allow for string to carry over to multiple lines
multi_line_quote = '''just 
like everyone else'''
#use this syntax to print multiple different types of strings
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
#including end="" allows multiple print statements to be printed on one line
print("I don't like ", end="")
print("newlines")
#print multiple newlines
print('\n' * 5)
#print specific characters within a string
long_string = 'It\'s a groundhog life.'
print(long_string[0:4])
#print last five characters of a string
print(long_string[-5:])
#print up to a certain character in a string
print(long_string[:-5])
#concatenate strings
print(long_string[:2] + ' makes for a questionable sanity.')
#or
character = 'K'
string = 'favorite'
number = 3
print("%c is my %s letter and the number %d is my favorite number." % (character, string, number))
#capitalize first letter of a string
print(long_string.capitalize())
#return first index of a specified character
print(long_string.find('g'))