# T = int(input())
# for tc in range(1, T+1):
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    a=[]
    # 가로 검사
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                for p in range(M):
                    a.append(arr[i][j+p])
    # 세로 검사
    if a:
        print(f"#{tc} {''.join(a)}")
    else:
        for i in range(N):
            for j in range(N-M+1):
                for k in range(M):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        break
                else:
                    for p in range(M):
                        a.append(arr[j + p][i])
        print(f'#{tc} {"".join(a)}')



