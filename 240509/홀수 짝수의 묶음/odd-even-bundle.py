# 변수 선언 및 입력
n = int(input())
blocks = list(map(int, input().split()))

even = 0
odd = 0
for block in blocks:
    if(block % 2 == 0):
        even += 1
    else:
        odd += 1


group_num = 0
while True:
    if group_num % 2 == 0:
        if even:
            even -= 1
            group_num += 1
        elif odd >= 2:
            odd -= 2
            group_num += 1
        else:
            if even > 0 or odd > 0:
                group_num -= 1

            break

    else:
        if odd:
            odd -= 1
            group_num += 1
        else:
            break

print(group_num)