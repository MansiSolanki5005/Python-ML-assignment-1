#Question5- Write a program that takes a string input from the user and writes it to a text file.

user_input = input('Enter a string: ')
with open('user_input.txt', 'w') as file:
    file.write(user_input)

print('Your input has been written in the file "user_input".')
