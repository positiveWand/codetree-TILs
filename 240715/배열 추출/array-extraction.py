import heapq
n = int(input())
nums = []
for _ in range(n):
    num = int(input())

    if num == 0:
        if nums:
            print(-heapq.heappop(nums))
        else:
            print(0)
    else:
        heapq.heappush(nums, -num)