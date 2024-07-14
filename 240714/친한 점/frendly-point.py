n, m = list(map(int, input().split()))

points = []
for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)

points.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

for _ in range(m):
    query = tuple(map(int, input().split()))
    i = binary_search(points, query)

    if i < len(points):
        print(points[i][0], points[i][1])
    else:
        print(-1, -1)