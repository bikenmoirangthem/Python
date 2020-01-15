# Python Program to find HCF/GCD of two numbers

# Function to find HCF/GCD
# HCF/GCD of two numbers doesn’t change 
# if smaller number is subtracted from a bigger number.

def hcf(num1, num2):
    if (num1 == 0 or num2 == 0):
        return False
    if (num1 == num2):
        return num1
    
    if (num1 > num2):
        return hcf(num1 - num2, num2)
    return hcf(num1, num2 - num1)

num1 = 10
num2 = 30
if hcf(num1, num2):
    print("The HCF of",num1,"and",num2, "is", hcf(num1, num2))
else:
    print("no hcf")