# Python program to find factors of a number

# function to find factors
def factors(n):
    print("The factors of", n, "are:")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end="\t")

num = int(input("Enter any number to find factors: "))
factors(num)