import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0]*(V + 1) for _ in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
        adjM[e][s] = w

    mst = set()
    weights = [0xffffff] * (V+1)
    weights[0]= 0
    while len(mst) <= V:
        minV = 0xffffff
        min_idx = 0
        for i in range(V+1):
            if i not in mst and weights[i] < minV:
                minV = weights[i]
                min_idx = i
        mst.add(min_idx)
        for i in range(V+1):
            if i not in mst and adjM[min_idx][i] and adjM[min_idx][i] < weights[i]:
                weights[i] = adjM[min_idx][i]
    print(f'#{tc} {sum(weights)}')



