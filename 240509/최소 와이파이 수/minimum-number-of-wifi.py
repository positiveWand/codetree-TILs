n, m = tuple(map(int, input().split()))
status = list(map(int, input().split()))

current = 0
before_count = -1
wifi = 0
while current < n:
    count = 0
    for s in status[max(0, current-m):min(n, current+m)]:
        if s == 1:
            count += 1
    
    if before_count < count and current+m < n:
        current = current+1
        before_count = count
    else:
        current = current+m
        wifi += 1
        before_count = -1

print(wifi)