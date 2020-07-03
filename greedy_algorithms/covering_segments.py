'''
# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
'''
# python3
n = int(input())
lst = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    lst.append((a,b))

lst.sort(key = lambda x: x[1])

index = 0
coordinates = []

while index < n:
    curr = lst[index]
    while index < n-1 and curr[1]>=lst[index+1][0]:
        index += 1
    coordinates.append(curr[1])
    index += 1
print(len(coordinates))
print(' '.join([str(i) for i in coordinates]))
