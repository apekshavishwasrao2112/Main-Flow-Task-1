# TASK-1 PYTHON PROGRAMMING.


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

