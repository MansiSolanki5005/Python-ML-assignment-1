#Question19- Write a python program that removes all punctuation from a given string.

str1= input('Enter the string: ')
punc= '''!()-[]\{};:'",<>./?@#$%^&*_~''' # type: ignore
res= " "
for ele in str1:
	if ele not in punc:
		res+= ele
print("The string after punctuation filter : " ,res)
