# TASK-1 PYTHON PROGRAMMING.


#6. Palindrome check

def is_palindrome(s):
    return s == s[::-1]  # Compare the string with its reversed version


string = input("Enter a string: ")


if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
