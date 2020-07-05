'''# Uses python3
import sys

def get_change(m):
    #write your code here
    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

import math

money = int(input())
denominations = [1, 3, 4]
minCoins = [0] + [math.inf]*money

for i in range(1, money+1):
    print(' for i=',i)
    for j in denominations:
        print(' for j=',j)
        if i>=j:
            print('if1')
            coins = minCoins[i-j]+1
            print('coins=', coins)
            if coins < minCoins[i]:
                print('if2')
                minCoins[i] = coins
                print(minCoins)

print(minCoins[money])

n=3
nums=[n]
nums += [2,6]
print(nums)
print(' '.join([str(i) for i in nums][::-1]))
'''
import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
num_operations = [0, 0] + [math.inf]*(n-1)
print(num_operations)
for i in range(2, n+1):
    print('for i=', i)
    temp1, temp2, temp3 = [math.inf]*3

    temp1 = num_operations[i-1] + 1 
    if i%2 == 0: temp2 = num_operations[i//2] + 1
    if i%3 == 0: temp3 = num_operations[i//3] + 1
    min_ops = min(temp1, temp2, temp3)
    print(min_ops)
    num_operations[i] = min_ops

print(num_operations[n])

# Backtracking the numbers leading to n
nums = [n]
while n!=1:
    if n%3 ==0 and num_operations[n]-1 == num_operations[n//3]:
        nums += [n//3]
        n = n//3
    elif n%2 ==0 and num_operations[n]-1 == num_operations[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))
