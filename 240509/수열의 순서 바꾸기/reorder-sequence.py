N = int(input())

arr = map(int, input().split())

count = 1
for i in range(N-1, -1, -1):
    if i == N-1:
        continue
    
    if arr[i] <= arr[i+1]:
        count += 1
    else:
        # print(arr[i], arr[i+1])
        # print(arr[i] > arr[i+1])
        # print(i)
        break

print(count)

print(N-count)