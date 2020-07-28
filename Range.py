# Get range list using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionRange(n):
    if n == 0:
        return [0]
    elif n < 0:
        return [n] + RecursionRange(n+1) 
    elif n > 0:
        return RecursionRange(n-1) + [n]

print(RecursionRange(10))