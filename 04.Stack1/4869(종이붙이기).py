def sol(n):
    if n==10:
        return 1
    if n==20:
        return 3
    return sol(n-10)*1 + sol(n-20)*2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {sol(N)}')