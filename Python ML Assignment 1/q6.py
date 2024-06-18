#Question6- Write a program that reads the content of a text file and prints it to the console.

with open('user_input.txt', 'r') as file:
    content = file.read()

print('The content of the text file "user_input" is: ',content)