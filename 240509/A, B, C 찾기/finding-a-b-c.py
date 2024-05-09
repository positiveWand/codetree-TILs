arr = list(map(int, input().split()))

arr.sort()
arr.remove(arr[0]+arr[1])
print(arr[0],arr[1],arr[2])