N = int(input())

arr = input().split()

count = 1
for i in range(N-1, -1, -1):
    if i == N-1:
        continue
    
    if arr[i] <= arr[i+1]:
        count += 1
    else:
        break

print(N-count)