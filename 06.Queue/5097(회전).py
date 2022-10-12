import sys
sys.stdin = open('input.txt', 'r')

def rotate(q,M):
    cnt = 0
    pin = 0
    while True:
        if cnt ==M:
            return q[pin]
        pin = (pin+1)%N
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    print(f'#{tc} {rotate(q, M)}')