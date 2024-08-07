n, m = list(map(int, input().split()))

def bisect_right(lst, element):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right-left)//2
        if lst[mid] <= element:
            left = mid+1
        else:
            right = mid-1
    
    return left

def bisect_left(lst, element):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right-left)//2
        if lst[mid] < element:
            left = mid+1
        else:
            right = mid-1
    
    return left

nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()

answer = float('inf')
for num in nums:
    lowerbound = num + m
    upperbound = num - m
    right = bisect_left(nums, lowerbound)
    left = bisect_left(nums, upperbound)

    # print(right, left)

    if 0<=right<len(nums):
        answer = min(answer, abs(num-nums[right]))
    if 0<left<len(nums):
        if nums[left] == num:
            answer = min(answer, abs(num-nums[left]))
        else:
            answer = min(answer, abs(num-nums[left-1]))

if answer != float('inf'):
    print(answer)
else:
    print(-1)