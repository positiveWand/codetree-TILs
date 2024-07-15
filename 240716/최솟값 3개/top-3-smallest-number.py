import heapq
n = int(input())
nums = list(map(int, input().split()))

heap = []
for n in nums:
    heapq.heappush(heap, n)
    if len(heap) < 3:
        print(-1)
    else:

        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        c = heapq.heappop(heap)

        print(a*b*c)

        heapq.heappush(heap, a)
        heapq.heappush(heap, b)
        heapq.heappush(heap, c)