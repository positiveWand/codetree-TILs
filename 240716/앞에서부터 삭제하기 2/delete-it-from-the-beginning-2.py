import heapq

N = int(input())
nums = list(map(int, input().split()))

sums = []
prev = 0
for n in nums:
    sums.append(prev + n)
    prev = prev + n

# print(sums)

# heap = [n for n in nums]
# heapq.heapify(heap)
# mins = []
# for n in nums:
#     current_min = heapq.heappop(heap)

#     if current_min != n:
#         heapq.heappush(heap, current_min)
    
#     mins.append(current_min)

# print(mins)
        

answer = -1
for k in range(1, N-2+1):
    target = nums[k:]
    min_num = min(target)

    answer = max(answer,(sums[-1] - sums[k-1] - min_num) / (len(target)-1))


print(f'{answer:.2f}')