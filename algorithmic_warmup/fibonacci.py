# Uses python3
'''
#using recursion
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
'''
'''
# using space optimum
def fibo(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        b, a = c, b
    print(c)

fibo(n)
'''
'''
def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

n = int(input())
print(calc_fib(n))
'''
f=[0,1]
def fibonacci(n):
    if (n<=1):
        return n
    else:
        for i in range(2,n+1):
            a=f[i-1] + f[i-2]
            f.append(a)
        return a
	  
		 
# Driver Program 
n = int(input())
print(fibonacci(n)) 

  
