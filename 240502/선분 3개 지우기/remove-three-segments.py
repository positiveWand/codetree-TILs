n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

answer = 0

# 서로 다른 3개의 선분을 제외하는 경우의 수 검사
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # 선분의 범위가 작음
            # 카운팅으로 겹침 검사 가능
            axis = [0 for _ in range(101)]
            for l in range(n):
                if l != i and l != j and l != k:
                    for m in range(lines[l][0], lines[l][1]+1):
                        axis[m] += 1
            
            fail = False
            for a in axis:
                if a >= 2:
                    fail = True
            if not fail:
                answer += 1

print(answer)