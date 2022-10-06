T = int(input())
for tc in range(1, T+1):
    word1 = input()
    word2 = input()
    word2_num = len(word2)
    maxV = 0
    idx = 0
    while True:
        if idx == len(word1):
            break
        cnt = 0
        for el in word2:
            if el ==word1[idx]:
                cnt += 1
        if cnt > maxV:
            maxV = cnt
        idx += 1
    print(f'#{tc} {maxV}')

