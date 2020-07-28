# Sum all number up to nth number using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionSum(n):
    if n == 0: 
        return 0
    elif n > 0:
        return n + RecursionSum(n-1)
    elif n < 0:
        return n + RecursionSum(n+1)

n = 100
result = RecursionSum(n)
print(f'The Sum of all numbers up to {n} = {result}')
