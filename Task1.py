# TASK-1 PYTHON PROGRAMMING.

#1. The sum of two numbers

num1 =12
num2 =45

sum = num1 + num2

print(num1,"+",num2,"=",sum)


#2. odd or even

number = int(input("Enter a number:"))
if number % 2 == 0:
        print("Even")
else:
        print("Odd")


#3. Factorial Calculation

import math
n = int(input("Enter a number:"))
print(f"Factorial of {n} using math.factorial:{math.factorial(n)}")

#4. Fibonacci sequence
def fibonacci_sequence(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci


n = int(input("Enter the number of Fibonacci numbers to generate: "))


print(f"The first {n} Fibonacci numbers are: {fibonacci_sequence(n)}")


#5. reverse a string

def reverse_string(s):
    return s[::-1]  # This slices the string in reverse order.


string = input("Enter a string: ")

print(f"The reversed string is: {reverse_string(string)}")



#6.  Palindrome check

def is_palindrome(s):
    return s == s[::-1]  # Compare the string with its reversed version


string = input("Enter a string: ")


if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")


#7. Leap year check

    
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#8. Armstrong number check

def is_armstrong(n):
    num_str = str(n)  
    num_digits = len(num_str)  
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return n == sum_of_powers

n = int(input("Enter a number: "))

if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")





#1. custom Encryption - Decreption System

# Caesar Cipher Encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
           
            start = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
           
            encrypted_text += char
    return encrypted_text

# Caesar Cipher Decryption
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
          
            start = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
          
            decrypted_text += char
    return decrypted_text


message = input("Enter a message to encrypt: ")
shift = int(input("Enter shift value (integer): "))

encrypted_message = encrypt(message, shift)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted message: {decrypted_message}")





















