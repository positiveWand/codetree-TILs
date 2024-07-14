n,m= list(map(int, input().split()))

points = []
for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)

points.sort()

def bisect_left(lst, element):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right-left)//2
        if lst[mid] < element:
            left = mid+1
        else:
            right = mid-1
    
    return left

for _ in range(m):
    query = (int(input()), 0)

    target = bisect_left(points, query)
    if 0<=target<len(points):
        p = points.pop(target)
        print(p[0], p[1])
    else:
        print(-1, -1)