import heapq

N = int(input())
nums = list(map(int, input().split()))

answer = -1
for k in range(1, N-2+1):
    target = nums[k:]
    min_num = min(target)

    answer = max(answer,(sum(target) - min_num) / (len(target)-1))


print(f'{answer:.2f}')