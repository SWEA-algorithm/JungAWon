import sys
sys.stdin = open('input.txt', 'r')
for _ in range(10):
    tc = int(input())
    a = list(map(int, input().split()))
    idx = 0
    front = 0
    cnt = 0
    while True:
        a[idx] -= (cnt+1)
        cnt = (cnt + 1)%5
        front = (front + 1)%8
        if a[idx]<=0:
            a[idx]=0
            idx = (idx + 1)%8
            break
        idx = (idx + 1)%8
    ### 이 출력부분을
    print(f'#{tc}',end=' ')
    for i in range(idx,len(a)):
        print(a[i], end=' ')
    for i in range(idx):
        print(a[i], end=' ')
    print()
    ### 이렇게 풀어도 된다.
    print(f'#{tc}', end=' ')
    for _ in range(8):
        print(a[idx], end=' ')
        idx = (idx + 1)%8
    print()