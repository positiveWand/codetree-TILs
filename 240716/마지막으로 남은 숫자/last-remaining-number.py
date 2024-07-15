import heapq
n = int(input())
nums = list(map(lambda x: -int(x), input().split()))

heapq.heapify(nums)

while len(nums) >= 2:
    a = -heapq.heappop(nums)
    b = -heapq.heappop(nums)

    if a != b:
        heapq.heappush(nums, -abs(a-b))

if nums:
    print(-nums.pop())
else:
    print(-1)