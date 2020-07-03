'''
#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
'''    
# python3
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
ans = sum([a[i]*b[i] for i in range(n)])
print(ans)
