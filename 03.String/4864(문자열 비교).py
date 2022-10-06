T = int(input())
for tc in range(1, T+1):
    A = input()
    B = input()
    a = len(A)
    b = len(B)

    result = 0
    for i in range(b-a+1):
        for j in range(a):
            if A[j] != B[i+j]:
                break
        else:
            result = 1
            break
    print(f'#{tc} {result}')