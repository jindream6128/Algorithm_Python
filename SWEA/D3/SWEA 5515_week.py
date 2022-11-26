import sys
sys.stdin = open("input.txt", "r")

month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1,T+1):
    m ,d = map(int, input().split())
    # 2016년 m월d일 1월 1일은 금요일
    # 월0 화1 수2 목3 금4 토5 일6
    ans = 0
    for i in range(0,m-1):
        ans += month_day[i]
    ans += d+3
    print(f'#{tc} {ans%7}')
