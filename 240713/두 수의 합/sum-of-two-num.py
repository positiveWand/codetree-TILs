n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

count = {}
for n in nums:
    if n not in count:
        count[n] = 0
    count[n] += 1

answer = 0
used = set()
for num in count.keys():
    if num in used:
        continue
    if (k - num) in count:
        used.add(num)
        used.add(k-num)
        answer += count[num] * count[k-num]

print(answer)