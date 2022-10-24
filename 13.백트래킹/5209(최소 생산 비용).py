def recur(row, sumV):
    global minV
    if sumV > minV:
        return
    if row == N:
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if check[i ]== 0:
            check[i] = 1
            recur(row + 1, sumV + arr[row][i])
            check[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    minV = 0xffff
    recur(0,0)
    print(f'#{tc} {minV}')