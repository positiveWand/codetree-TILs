n, m = tuple(map(int, input().split()))
inputs = list(map(int, input().split()))

class SortedList:
    def __init__(self, elements):
        self.arr = sorted(list(elements))
        # print(self.arr)
    
    def bisect_right(self, element):
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = left + (right-left)//2
            if self.arr[mid] <= element:
                left = mid+1
            else:
                right = mid-1
        
        return left
    
    def add(self, element):
        left = self.bisect_right(element)
        
        # self.arr[left:left] = [element]
        self.arr.insert(left, element)
        
        # print(self.arr)
    
    def size(self):
        return len(self.arr)
    
    def get(self, index):
        return self.arr[index]
    

sl = SortedList([])

answer = 0
for i in inputs:
    br = sl.bisect_right(i)
    # print(br)

    if br < i:
        sl.add(i)
        answer += 1
    else:
        break

print(answer)