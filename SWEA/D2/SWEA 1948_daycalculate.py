T = int(input())
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} # 각 월에 해당하는 day를 딕셔너리 형태로 저장

for test_case in range(1, T+1):
    monA, dayA, monB, dayB = map(int, input().split())
    ans = 0

    if monA == monB: # 같은 달이라면 단순히 dayB-dayA+1을 하면됨
        print(f'#{test_case} {dayB-dayA+1}')


    else: # 다른 달이라면,
        for i in range(monA+1, monB): # 사이에 달들의 day를 더한다
            ans += days[i]
        ans = ans+ (days[monA]-dayA+1) + dayB # ans = 사이day + 첫번째달 day + 마지막달 day
        print(f'#{test_case} {ans}')