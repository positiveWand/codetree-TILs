N, B = list(map(int, input().split()))
P = list()
S = list()
for _ in range(N):
    p, s = input().split()
    P.append(int(p))
    S.append(int(s))

answer = 0
# 할인할 선물 선택
for i in range(N):
    # 선물 수령 비용(= 선물값+배달비) 계산
    T = list()
    for j in range(N):
        if i == j:
            T.append(P[j]//2+S[j])
        else:
            T.append(P[j]+S[j])
            
    # 정렬 후 그리디하게 가능한 최대 학생 수 계산
    T.sort()
    subsum = 0
    price = list()
    for t in T:
        if t + subsum <= B:
            price.append(t)
            subsum += t
    
    # print(price)
    answer = max(answer, len(price))

print(answer)