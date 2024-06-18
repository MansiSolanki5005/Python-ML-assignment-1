'''Question17- Write a program in python that converts a given string to title case (i.e. 
first letter of each word capitalized).'''

def title(string):
    return string.title()

string1 = input('Input the string: ')
print('String converted to title case: ',title(string1))
