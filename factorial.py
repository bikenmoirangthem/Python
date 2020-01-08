#program to find factorial of a number

#function to find factorial
def find_factorial(x):
    factorial = 1
    if n<0:
        print('Factorial not exists for negetive number')
    elif n==0:
        print('Factorial of {} is {}'.format(n,factorial))
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        print('Factorial of {} is {}'.format(n,factorial))

#getting input from user
num = int(input('Enter the number you want to find factorial : '))

#calling factorial function
find_factorial(num)
