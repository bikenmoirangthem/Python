#program to reverse a string

#function to reverse a string
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str

#getting a string from user
str = input('Enter any string : ')

#printing the original string
print('Your original string : ',str)

#printing the reverse string
print('Reverse string : ',reverse(str))
