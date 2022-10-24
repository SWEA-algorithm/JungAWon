def bus2(idx, cnt, remain):
    global minV

    if cnt >= minV:
        return
    if idx == final:
        if cnt < minV:
            minV = cnt
        return
    bus2(idx + 1, cnt + 1, stops[idx]-1)
    if remain > 0:
        bus2(idx + 1, cnt, remain - 1)



T = int(input())
for tc in range(1, T+1):
    N, *stops = list(map(int, input().split()))
    final = len(stops)
    minV = 0xfffff
    bus2(0, 0, stops[0])
    print(f'#{tc} {minV}')