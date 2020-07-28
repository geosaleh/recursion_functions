# Calculate n Fibonacci number using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionFibonacci(n, a = 0, b = 1):
    if n == 0: 
        return a 
    if n == 1: 
        return b 
    return RecursionFibonacci(n - 1, b, a + b);

n = 50
result = RecursionFibonacci(n)
print(f'Fibonacci # {n} = {result}')