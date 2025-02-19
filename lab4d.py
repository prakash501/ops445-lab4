#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_str):
    """Returns the first five characters of the input string."""
    return input_str[:5]

def last_seven(input_str):
    """Returns the last seven characters of the input string."""
    return input_str[-7:]

def middle_number(input_num):
    """Returns the second and third characters of the input number (as a string)."""
    num_str = str(input_num)  # Convert the number to a string
    return num_str[1:3]       # Return the second and third characters

def first_three_last_three(str1, str2):
    """Returns a string that combines the first three characters of str1 and the last three characters of str2."""
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))  # Expected Output: 'Hello'
    print(first_five(str2))  # Expected Output: 'Senec'
    print(last_seven(str1))  # Expected Output: 'World!!'
    print(last_seven(str2))  # Expected Output: 'College'
    print(middle_number(num1))  # Expected Output: '50'
    print(middle_number(num2))  # Expected Output: '.5'
    print(first_three_last_three(str1, str2))  # Expected Output: 'Helege'
    print(first_three_last_three(str2, str1))  # Expected Output: 'Send!!'

