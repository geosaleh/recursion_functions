# Calculate the greatest common divisor (gcd) using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionGCD(p, q):
        if q == 0:
            return p
        else:
            return RecursionGCD(q, p % q)

a=5
b=15
result = RecursionGCD(a,b)
print(f'The GCD of ({a} & {b}) = {result}')