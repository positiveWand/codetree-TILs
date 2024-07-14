n, m = tuple(map(int, input().split()))
inputs = list(map(int, input().split()))

class SortedSet:
    def __init__(self, elements):
        self.set = set(elements)
        self.lst = list(self.set)
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
        self.set.add(item)
        self.lst.insert(self.bisect_right(item), item)
    
    def remove(self, item):
        self.set.remove(item)
        target = self.bisect_right(item) - 1
        if 0<=target<len(self.lst) and self.lst[target] == item:
            self.lst.pop(target)
    
    def get(self, index):
        return self.lst[index]


seats = SortedSet(list(range(1, m+1)))

answer = 0
for i in inputs:
    idx = seats.bisect_right(i)

    if idx != 0:
        idx -= 1
        seats.remove(seats.get(idx))

        answer += 1
    else:
        break

print(answer)