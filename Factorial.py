# Calculate Factorial using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionFactorial(n):
    if n == 1:
        return 1
    else:
        return n * RecursionFactorial(n-1)
    
n = 7
result = RecursionFactorial(n)
print(f'Factorial of {n} = {result}')