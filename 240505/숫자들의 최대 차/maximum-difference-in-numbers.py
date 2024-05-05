N, K = list(map(int, input().split()))
nums = [int(input()) for _ in range(N)]

answer = 0
for min_num in nums:
    count = 0
    for num in nums:
        if min_num <= num <= min_num+K:
            count += 1
    answer = max(answer, count)

print(answer)