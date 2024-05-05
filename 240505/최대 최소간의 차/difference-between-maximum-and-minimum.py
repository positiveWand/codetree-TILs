n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = float('inf')
for min_num in range(1, 10001):
    cost = 0

    for num in nums:
        if num < min_num:
            cost += abs(min_num-num)
        elif min_num+k < num:
            cost += abs(min_num+k-num)

    answer = min(answer, cost)

print(answer)