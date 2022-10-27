import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [-1]*1000001
    deck = [N]
    idx = 0
    visited[N] = 0
    while True:
        if visited[M] != -1:
            break
        N = deck[idx]
        for i in range(4):
            if i == 0:
                temp = N + 1
            elif i == 1:
                temp = N - 1
            elif i == 2:
                temp = N * 2
            else:
                temp = N - 10
            if 0 < temp <= 1000000 and visited[temp] == -1:
                visited[temp] = visited[N] + 1
                deck.append(temp)
        idx += 1
    print(f'#{tc} {visited[M]}')




