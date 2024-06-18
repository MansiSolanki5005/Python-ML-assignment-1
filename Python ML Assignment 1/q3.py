# Question3- Write a program that calculates the factorial of a given number.

a=int(input('Enter the number:'))
b=1
for i in range(1,a+1):
    b*=i
print('The factorial of the number is: ',b)
