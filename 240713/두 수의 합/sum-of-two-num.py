n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

count = {}
for n in nums:
    if n not in count:
        count[n] = 0
    count[n] += 1

answer = 0
for i, n in enumerate(nums):
    if (k - n) in count and count[k-n] >= 1:
        count[n] -= 1
        answer += count[k-n]

print(answer)