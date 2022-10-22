#1개의 리스트를 2개의 리스트로 나누고 정렬해 반환하는 함수
def merge_sort(lst):
    global cnt
    N = len(lst)
    if N == 1:
        return lst
    # 중앙 분기점을 잡고
    middle = N//2
    #2개의 리스트로 나누기
    left = lst[:middle]
    right = lst[middle:]
    # 리스트의 요소가 1개일때까지 2개의 리스트로 나누는 걸 반복
    left = merge_sort(left)
    right = merge_sort(right)
    #각 left와 right에 접근하는인덱스 i와 j에 대해 인덱스와 리스트의 길이를 비교해가며 모든 리스트에 접근할 수 있는지를 확인
    i = j = 0
    temp = []
    if left[-1] > right[-1]:
        cnt += 1

    while i<len(left) or j <len(right):
        if i<len(left) and j<len(right):
            if left[i]<right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        elif i>=len(left):
            temp.append(right[j])
            j += 1
        elif j >=len(right):
            temp.append(left[i])
            i += 1
    return temp

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[N//2]} {cnt}')