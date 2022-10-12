import sys
sys.stdin = open('input.txt', 'r')
delta = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(start):
    check = [[0]*N for _ in range(N)]
    q = []
    q.append(start)
    check[start[0]][start[1]] = 1
    while q:
        r, c = q.pop(0)
        if board[r][c]==3:
            return check[r][c] -2
        for d in delta:
            nr, nc = r + d[0], c + d[1]
            if 0<=nr<N and 0<=nc<N and (board[nr][nc]==0 or board[nr][nc]==3) and check[nr][nc]==0:
                q.append((nr, nc))
                check[nr][nc] = check[r][c] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]==2:
                start = (i, j)
    print(f'#{tc} {bfs(start)}')
