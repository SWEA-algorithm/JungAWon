T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N
    a.sort()
    a1 = a[:N//2]
    a.sort(reverse=True)
    a2 = a[:N//2]
    for i in range(N//2):
        b[2*i] = a2[i]
        b[2*i+1] = a1[i]
    print(f'#{tc}',end=' ')
    print(*b[:10])
    '''
    원본 인덱스를 잘 정리: k, N-1-k라는 두 인덱스로 움직인다
    '''

