#Question16- Write a program in python that counts the frequency of each character in a string.

string=input('Enter the string: ')
freq = {}

for i in string:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

print("Count of all characters is :\n ", str(freq))
