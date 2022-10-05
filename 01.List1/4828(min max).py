T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    result = A[-1]-A[0]
    print(f'#{tc} {result}')
##########################################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    minV = 1000001
    maxV = 0
    for i in range(N):
        if minV > A[i]:
            minV = A[i]
        if maxV < A[i]:
            maxV = A[i]
    print(f'#{tc} {maxV - minV}')