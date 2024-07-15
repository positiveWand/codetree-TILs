import heapq
n = int(input())

nums = []

for i in range(n):
    n = int(input())

    if n == 0:
        if nums:
            print(heapq.heappop(nums)[1])
        else:
            print(0)
    else:

        heapq.heappush(nums, (abs(n), n))