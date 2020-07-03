#Uses python3
'''
import sys

def largest_number(a):
    #write your code here
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

n = int(input())
lst = [int(i) for i in input().split()]


def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer

print(''.join([str(i) for i in largestnumber(lst)]))
'''
import sys

def IsGreaterOrEqual(digit, max_digit):
    #check both the combinations digit_max_digit and max_digit_digit
    return int((digit)+(max_digit))>=int((max_digit)+(digit))

    
def largest_number(a):
    result = []
    
#     a = sorted(a, key = lambda x: int(x[0]), reverse=True)
    while a:
        max_digit = '0'
        for digit in a:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        result.append(max_digit)
        a.remove(max_digit)

    res = ""
    for x in result:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

'''
def largest_number(a):
    result=[]
    while a:
        x=max(a)
        result.append(x)
        a.remove(x)
        
    #return result
    res = ""
    for x in result:
        res += x
    return res

    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
'''
