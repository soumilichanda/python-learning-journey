# 1. Countdown using recursion
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

# 2. Factorial using recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 3. Sum of first N numbers
def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)

# 4. Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 5. Reverse a string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Extra: Power(a, b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

if __name__ == "__main__":
    print("=== Recursion Practice ===")

    # 1. Countdown
    cd_input = int(input("Enter starting number for countdown: "))
    countdown(cd_input)

    # 2. Factorial
    fact_input = int(input("\nEnter an integer for factorial: "))
    print(f"Factorial of {fact_input}:", factorial(fact_input))

    # 3. Sum of N numbers
    sum_input = int(input("\nEnter N to find sum of first N numbers: "))
    print(f"Sum of first {sum_input} numbers:", sum_n(sum_input))

    # 4. Fibonacci
    fib_input = int(input("\nEnter index for Fibonacci: "))
    print(f"Fibonacci({fib_input}):", fibonacci(fib_input))

    # 5. Reverse string
    str_input = input("\nEnter a string to reverse: ")
    print("Reversed string:", reverse_string(str_input))

    # Extra: Power(a, b)
    base = int(input("\nEnter base (a): "))
    exp = int(input("Enter exponent (b): "))
    print(f"{base}^{exp}:", power(base, exp))