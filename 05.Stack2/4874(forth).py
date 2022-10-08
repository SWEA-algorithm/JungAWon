def sol(data):
    for i in range(len(a)):
        if a[i].isdigit():
            stack.append(int(a[i]))
        elif a[i] in '+-*/':
            if len(stack) >= 2:
                n2 = stack.pop()
                n1 = stack.pop()
                if a[i] == '+':
                    n3 = n1 + n2
                elif a[i] == '-':
                    n3 = n1 - n2
                elif a[i] == '*':
                    n3 = n1 * n2
                elif a[i] == '/':
                    n3 = n1 // n2
                stack.append(n3)
            else:
                return 'error'
        elif a[i] == '.':
            break
    if len(stack)==1:
        return stack.pop()
    else:
        return 'error'


T = int(input())
for tc in range(1, T+1):
    a = list(input().split())
    stack = []
    print(f'#{tc} {sol(a)}')
'''
pop()할때 2개이상이면 pop()하기
. 이후에 1개만 남았을때가 error 안남는 상황
'''

