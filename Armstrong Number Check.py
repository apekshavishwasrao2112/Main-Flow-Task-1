# TASK-1 PYTHON PROGRAMMING.

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



