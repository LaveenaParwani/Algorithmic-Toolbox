# Uses python3
import sys
'''
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
'''
'''
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
#         print('now',a[left])
        return a[left]
#     print('call 1')
    left_elem = get_majority_element(a, left, (left+right+1)//2)
#     print('call 2')
    right_elem = get_majority_element(a, (left+right+1)//2, right)

    lcount = 0
#     print('left_elem',left_elem)
#     print('right_elem',right_elem)
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

 
'''
'''
#print("Hello World")
# Uses python3
import sys

def get_majority_element(a, left, right):
    print("main")
    if left == right:
        return -1
    if left + 1 == right:
        print('now',a[left])
        return a[left]
    print('call 1')
    print("left:" ,left, "right:",right) 
    left_elem = get_majority_element(a, left, (left+right+1)//2)
    print('call 2')
    print("left:" ,left, "right:",right) 
    right_elem = get_majority_element(a, (left+right+1)//2, right)
    print("left:" ,left, "right:",right)


    lcount = 0
    print("lcount", lcount)
    print('left_elem',left_elem)
    print('right_elem',right_elem)
    for i in range(left, right):
        print("for1", "left:", left, "right:", right))
        if a[i] == left_elem:
            print("if for 1")
            lcount += 1
    if lcount > (right - left) // 2:
        print("if2 for 1")
        return left_elem

    rcount = 0  
    print("rcount", rcount)
    for i in range(left, right):
        print("for2", "left:", left, "right:", right)
        if a[i] == right_elem:
            print("if for 2")
            print("ooleft:" ,left, "right:",right)
            rcount += 1
    if rcount > (right - left) // 2:
        print("if2 for 2")
        return right_elem

    return -1


if __name__ == '__main__':
    input = input()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
'''
# Uses python3
import sys

def get_majority_element(a,n):
    maximum = a[0]
    amount = 1
    for i in (a[1:]):
        if not  maximum == i:
            if amount >= 1:
                amount = amount - 1
            else:
                maximum = i
                amount = 1
        else:
            amount = amount + 1
    output = a.count(maximum)
    if output > n//2:
        return 1
    return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print (get_majority_element(a,n))

