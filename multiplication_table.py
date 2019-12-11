#program to print multiplication table of a number

#function to print multiplication table
def multiplication(num):
    print('Multiplication table of {}'.format(num))
    for i in range(1,n+1):
        print(' {}\tx\t{}\t=\t{}'.format(num,i,num*i))

#getting input from user       
num = int(input('Enter number to print multiplication table: '))

#calling multiplication function to print the table
multiplication(num)