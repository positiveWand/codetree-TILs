n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

count = {}
for n in nums:
    if n not in count:
        count[n] = 0
    count[n] += 1

answer = 0
for i in range(len(nums)):
    n = nums[i]
    count[n] -= 1

    for j in range(i):
        m = nums[j]

        if (k - n - m) in count:
            answer += count[k-n-m]
        
        

print(answer)