T = int(input())
for tc in range(1, T+1):
    N = int(input())
    timetable = [[0]*2 for _ in range(N)]
    for i in range(N):
        timetable[i][0], timetable[i][1] = map(int, input().split())
    timetable.sort(key=lambda x: x[1])
    cnt = 1
    a = timetable[0][1]
    for i in range(1, N):
        if a <= timetable[i][0]:
            cnt += 1
            a = timetable[i][1]
    print(f'#{tc} {cnt}')