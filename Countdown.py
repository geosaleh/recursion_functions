# Countdown using recursion
#
# follow us on twitter @PY4ALL
#

def RecursionCountdown(n):
    if n == 0:
        print(f'Go!')
    else:
        print(f'Countdown {n}')
        RecursionCountdown(n-1)
        
RecursionCountdown(5)