#Question21- Write a python program that counts the occurrences of a specific element in a list.

lst=input('Enter the list: ')
lst1=list(lst)
ele=input('Enter the element whose occurrence frequency is to be found: ')
count = 0
for i in lst:
    if (i == ele):
        count = count + 1
print('The frequency of occurrence of {ele} is: ',count)
