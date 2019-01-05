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
