#program to find fibonacci series upto nth term

#function to find fibonacci series
def fibonacci(n): 
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

#getting input from user
n = int(input('Enter the number of terms : '.format(n)))

print('Fibonacci series upto {}th term: '.format(n))

#printing the fibonacci series
for i in range(n+1):
    print(fibonacci(i),end='\t')

'''
i = 0
while (i<n+1):
    print(fibonacci(i),end='\t')
    i=i+1
'''
