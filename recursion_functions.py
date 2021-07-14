# Collection of different recursion functions
#
# follow us on twitter @PY4ALL
#

# Sum all number up to nth number using recursion
def recursion_sum(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + recursion_sum(n-1)
    elif n < 0:
        return n + recursion_sum(n+1)


# Calculate the greatest common divisor (gcd) using recursion
def recursion_GCD(p, q):
        if q == 0:
            return p
        else:
            return recursion_GCD(q, p % q)


# Calculate n Fibonacci number using recursion
def recursion_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return recursion_fibonacci(n - 1, b, a + b)


# Calculate Factorial using recursion
def recursion_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursion_factorial(n-1)


# Countdown using recursion
def recursion_countdown(n):
    if n == 0:
        print(f'Go!')
    else:
        print(f'Countdown {n}')
        recursion_countdown(n-1)


def main():
    # Test recursion_sum function
    n = 100
    result = recursion_sum(n)
    print(f'The Sum of all numbers up to {n} = {result}')

    # Test recursion_GCD function
    a = 5
    b = 15
    result = recursion_GCD(a, b)
    print(f'The GCD of ({a} & {b}) = {result}')

    # Test recursion_fibonacci function
    n = 50
    result = recursion_fibonacci(n)
    print(f'Fibonacci # {n} = {result}')

    # Test recursion_factorial function
    n = 7
    result = recursion_factorial(n)
    print(f'Factorial of {n} = {result}')
    
    # Test recursion_countdown function
    n = 5
    print(f'Test countdown for n = {n}')
    recursion_countdown(n)


if __name__ == "__main__":
    main()
