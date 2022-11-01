for test_case in range(1, 11):
    N = int(input())
    high = list(map(int, input().split()))
    ans = 0

    for i in range(2,N-2):
        left1 = high[i]-high[i-1]
        left2 = high[i]-high[i-2]
        right1 = high[i]-high[i+1]
        right2 = high[i]-high[i+2]
        if left1 > 0 and left2 > 0 and right1 > 0 and right2 > 0 :
            ans = min(left1, left2, right1, right2)
    # for i in range(2, N-2):
    #     #왼쪽 -1, 왼쪽 -2, 오른쪽 +1, 오른쪽 +2 가 만족하는지 검사
    #     if high[i]-high[i-1] > 0 and high[i]-high[i-2] > 0 and high[i]-high[i+1] > 0 and high[i]-high[i+2] > 0:
    #         mid.append(high[i]-high[i-1])
    #         mid.append(high[i]-high[i-2])
    #         mid.append(high[i]-high[i+1])
    #         mid.append(high[i]-high[i+2])
    #         ans = min(mid)
    #     else:
    #         pass
    # print(f'#{test_case} {ans}')
