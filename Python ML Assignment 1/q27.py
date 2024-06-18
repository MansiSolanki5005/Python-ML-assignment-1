#Question27- Write a program in python that converts a string into a list of its characters.

str1= input('Enter the string: ')
lst=[]
for i in str1:
    lst.append(i)
print('The list of characters of the string is: ',lst)