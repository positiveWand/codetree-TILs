n = int(input())
nums = list(map(int, input().split()))

answer = float('inf')
# 2배 할 원소와 제외할 원소 선택 후 시험
for i in range(n):
    doubled_nums = [num if idx != i else 2 * num for idx, num in enumerate(nums)]
    # print(doubled_nums)

    for j in range(n):
        eliminated = [num for idx, num in enumerate(doubled_nums) if idx != j]
        # print(eliminated)
        
        diff_sum = 0
        for k in range(len(eliminated)-1):
            diff_sum += abs(eliminated[k]-eliminated[k+1])

        answer = min(answer, diff_sum)

print(answer)