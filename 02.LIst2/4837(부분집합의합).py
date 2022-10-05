A = [1,2,3,4,5,6,7,8,9,10,11,12]
a = len(A)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    total_sub_set = []
    for i in range(1<<a):
        sub_set = []
        for j in range(a):
            if i&(1<<j):
                sub_set.append(A[j])
        total_sub_set.append(sub_set)
    cnt = 0
    for el in total_sub_set:
        if len(el) == N and sum(el)==K:
            cnt += 1
    print(f'#{tc} {cnt}')
