# Uses python3
'''import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum1      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        sum1 = (sum1 + current)%10

    return sum1 % 10

def fibonacci_sum_last_digit(n):
    time_period = 60
    index = n%time_period
#     print(index)
    if index<1:
        return index
    prev,curr = 0,1
    sum1      = 1
    for i in range(2, index+1):
        prev,curr = curr, (curr+prev)%10
        sum1 = (sum1 + curr)%10
    return sum1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
'''
n = int(input())

if n<=1:
    print(n)  
    quit()


lesser = (n+2)%60
if lesser==1:
    print(0)
    quit()
elif lesser==0:
    print(9)
    quit()
def fibo(n):
    a,b = 0, 1
    for _ in range(2,lesser+1):
        c = a+b
        c = c%10
        b, a = c, b
    if c!=0:
        print(c-1)
    else:
        print(9)
fibo(lesser)
