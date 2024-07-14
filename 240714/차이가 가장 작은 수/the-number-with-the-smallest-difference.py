n, m = list(map(int, input().split()))

class SortedList:
    def __init__(self, items):
        self.lst = list(items)
        self.lst.sort()
    
    def bisect_right(self, element):
        left = 0
        right = len(self.lst) - 1

        while left <= right:
            mid = left + (right-left)//2
            if self.lst[mid] <= element:
                left = mid+1
            else:
                right = mid-1
        
        return left
    
    def add(self, item):
        self.lst.insert(self.bisect_right(item), item)
    
    def remove(self, item):
        target = self.bisect_right(item) - 1
        if 0<=target<len(self.lst) and self.lst[target] == item:
            self.lst.pop(target)
    
    def get(self, index):
        return self.lst[index]
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