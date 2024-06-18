#Question11- Write a python program that generates the first n numbers in the Fibonacci sequence.

def fibo(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fibo(num-2)+fibo(num-1)

n = int(input('Enter value of n: '))
for i in range(0, n):
	print(fibo(i), end=" ")
