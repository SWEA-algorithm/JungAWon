import sys
sys.stdin = open('input.txt', 'r')
def tree(v,cnt):
    global cntV
    if c1[v]==0:
        if c2[v]==0:
            cntV = cnt
            return
        else:
            tree(c2[v],cnt+1)
    else:
        tree(c1[v],cnt+1)





T = int(input())
for tc in range(T):
    E, N = map(int,input().split())
    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    '''
    노드 번호와 인덱스의 갯수
    '''
    data = list(map(int, input().split()))
    for i in range(E):
        a, b = data[2*i], data[2*i+1]
        if c1[a]==0:
            c1[a]= b
        else:
            c2[a] = b
    cntV = 1
    tree(N,1)
    print(cntV)
    '''
    시간안에 못 풀었는데, 트리구조에서 순회를 이해하지 못한것으로 보임
    '''
