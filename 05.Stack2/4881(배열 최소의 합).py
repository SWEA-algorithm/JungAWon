def sol(r, sumV):
    global minV
    if sumV > minV:
        return
    if r==N:
        if sumV <minV:
            minV = sumV
        return
    for i in range(N):
        if visited[i]==0:
            visited[i] = 1
            sol(r+1, sumV + arr[r][i])
            visited[i]= 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited=[0]*N
    minV = 10*N
    sol(0,0)
    print(f'#{tc} {minV}')



