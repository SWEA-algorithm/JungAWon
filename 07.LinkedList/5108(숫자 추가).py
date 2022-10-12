import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    a =list(map(int, input().split())) + [0]*(N-M)
    for _ in range(M):
        idx, num = map(int, input().split())
        a.insert(idx, num)
    print(f'#{tc} {a[L]}')