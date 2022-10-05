T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    minV = 10000 * M
    maxV = 0
    for i in range(N-M+1):
        temp = 0
        for j in range(i,i+M):
            temp += a[j]
        if temp>maxV:
            maxV = temp
        if temp<minV:
            minV = temp
    print(f'#{tc} {maxV-minV}')
'''
구간의 인덱스 갯수에 유의할 것
'''
