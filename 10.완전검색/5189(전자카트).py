import sys
sys.stdin = open('input.txt', 'r')

def sol(row,sumV):
    global check, minV
    if sum(check)==N:
        if minV>sumV:
            minV = sumV
        return
    elif minV<sumV:
        return
    for i in range(N):
        if i==0 and 0 in check[1:]:
        # 조건 맞춰주기가 어려웠음, 0으로 가면 안되고, 또 N-1까지 가기전까지 0에 도달하면 안되기 떄문
            continue
        if i!= row and check[i]==0:
            check[i]=1
            sol(i, sumV+board[row][i])
            # row-i 니까 i-(또다른 i)로 가야한다.
            check[i]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    check = [0]*N
    minV = 0xffff
    sol(0,0)
    print(f'#{tc} {minV}')