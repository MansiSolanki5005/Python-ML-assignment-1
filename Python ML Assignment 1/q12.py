# Question12- Write a python program that calculates the sum of the digits of a given number.

num=input('Enter the number: ')
count=0
for i in num:
    count+= int(i)
print('Sum of digits is: ',count)
