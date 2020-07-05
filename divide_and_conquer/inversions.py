# Uses python3
import sys
'''
def get_num_of_inv_mid(a,b,left,mid,right):
    #left and right are already sorted
#     print('left',left,'mid',mid,'right',right)
    num_of_inv = 0
    i = left
    j = mid
    curr = left
    while i<(mid) and j<right+1:
        if a[i]<a[j]:
            b[curr] = a[i]
            i+=1
        else:
            b[curr] = a[j]
            j+=1
            num_of_inv += (mid-i-1)
#             print('\n',num_of_inv)
        curr+=1
    while i< mid:
        b[curr] = a[i]
        i+=1
        curr+=1
    while j<right+1:
#         print(curr)
        b[curr] = a[j]
        j+=1
        curr+=1
    for i in range(left,right):
        a[i] = b[i]
    return num_of_inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right>left:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, ave)
        number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
        number_of_inversions += get_num_of_inv_mid(a, b, left, ave+1, right)
    
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
'''
'''
def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    b = merge_sort(a[:mid])
    c = merge_sort(a[mid:])
    a_new = merge(b, c)
    return a_new


def merge(b, c):
    d = list()
    while (len(b) != 0) and (len(c) != 0):
        if b[0] <= c[0]:
            d.append(b[0])
            b = b[1:]
        else:
            d.append(c[0])
            c = c[1:]
    d.extend(b)
    d.extend(c)
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(merge_sort(a))
'''
'''
def get_num_of_inv_mid(a,b,left,mid,right):
    #left and right are already sorted
#     print('left',left,'mid',mid,'right',right)
    num_of_inv = 0
    i = left
    j = mid
    curr = left
    while i<(mid) and j<right+1:
        if a[i]<a[j]:
            b[curr] = a[i]
            i+=1
        else:
            b[curr] = a[j]
            j+=1
            num_of_inv += (mid-i-1)
#             print('\n',num_of_inv)
        curr+=1
    while i< mid:
        b[curr] = a[i]
        i+=1
        curr+=1
    while j<right+1:
#         print(curr)
        b[curr] = a[j]
        j+=1
        curr+=1
    for i in range(left,right):
        a[i] = b[i]
    return num_of_inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
    if right>left:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, ave)
#         print(number_of_inversions,'this1')
        number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
#         print(number_of_inversions,'this2')
        number_of_inversions += get_num_of_inv_mid(a,b,left,ave+1,right)
#         print(number_of_inversions,'this3')
        #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
    '''

def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = list()
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]
        
    return final, inversion_counter

def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    tot_count += temp

    return sorted_arr

tot_count = 0
n = int(input())
seq = [int(i) for i in input().split()]
mergesort(seq)
print(tot_count)

'''
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 
  
# Driver Code 
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(getInvCount(a, n)) 
'''
'''
def mergeSort(arr, n): 
    # A temp_arr is created to store 
    # sorted array in merge function 
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 
  
# This Function will use MergeSort to count inversions 
  
def _mergeSort(arr, temp_arr, left, right): 
  
    # A variable inv_count is used to store 
    # inversion counts in each recursive call 
  
    inv_count = 0
  
    # We will make a recursive call if and only if 
    # we have more than one elements 
  
    if left < right: 
  
        # mid is calculated to divide the array into two subarrays 
        # Floor division is must in case of python 
  
        mid = (left + right)//2
  
        # It will calculate inversion counts in the left subarray 
  
        inv_count += _mergeSort(arr, temp_arr, left, mid) 
  
        # It will calculate inversion counts in right subarray 
  
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
  
        # It will merge two subarrays in a sorted subarray 
  
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
# This function will merge two subarrays in a single sorted subarray 
def merge(arr, temp_arr, left, mid, right): 
    i = left     # Starting index of left subarray 
    j = mid + 1 # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray 
    inv_count = 0
  
    # Conditions are checked to make sure that i and j don't exceed their 
    # subarray limits. 
  
    while i <= mid and j <= right: 
  
        # There will be no inversion if arr[i] <= arr[j] 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array 
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 
  
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    result = mergeSort(a, n) 
    print(result) 
  
'''
