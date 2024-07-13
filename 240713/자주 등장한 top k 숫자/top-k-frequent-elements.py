n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

count = {}
for n in nums:
    if n not in count:
        count[n] = 1
    count[n] += 1

arr = []
for key, value in count.items():
    arr.append((value, key))

arr.sort(reverse=True)
# print(arr[-k:])

arr = map(lambda x: str(x[1]), arr[:k])
print(' '.join(arr))