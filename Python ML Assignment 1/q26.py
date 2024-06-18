'''Question26- Write a program in python that checks if a string starts with a given prefix 
or ends with a given suffix.'''

def check_string(given, prefix, suffix):
    return given.startswith(prefix) or given.endswith(suffix)

str1=input('Enter the string: ')
print(check_string(str1, 'h', 'i')) 