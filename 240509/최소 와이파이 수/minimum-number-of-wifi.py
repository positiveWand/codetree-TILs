n, m = tuple(map(int, input().split()))
status = list(map(int, input().split()))

current = 0
before_count = 0
wifi = 0
while current < n:
    count = 0
    for s in status[max(0, current-m):min(n, current+m)]:
        if s == 1:
            count += 1
    
    if before_count < count:
        current = current+1
        before_count = count
    else:
        current = current+m
        if count > 0:
            wifi += 1
        before_count = 0

print(wifi)