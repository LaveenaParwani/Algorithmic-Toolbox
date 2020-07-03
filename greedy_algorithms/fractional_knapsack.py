# Uses python3
import sys
'''
def get_optimal_value(capacity, weights, values):
    unit_value = [a/b for a,b in zip(values,weights)]
    unit_value = sorted(unit_value, key=int, reverse=True)
    m = len(unit_value)

    if capacity == 0: return []
    for i in range(0,m):
        if weights[i] > capacity: return unit_value[i]*capacity
        if weights[i] <= capacity: return values[i] + get_optimal_value(capacity-weights[i], weights, values)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
'''
n, W = [int(i) for i in input().split()]
lst = []

if W == 0:
    print(0)
    quit()

for _ in range(n):
    v, w = [int(i) for i in input().split()]
    if v == 0:
        continue
    lst.append((v, w))

lst.sort(key = lambda x: x[0]/x[1], reverse = True)

total_value = 0

for v,w in lst:
    if W==0:
        print(total_value)
        quit()
    amt = min(w, W)
    total_value += amt*v/w
    W -= amt

print(total_value)
