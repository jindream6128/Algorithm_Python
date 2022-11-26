# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    money = list(map(int, input().split()))
    cnt = 0
    for i in range(0,N):
        if money[i] <= sum(money)/N :
            cnt += 1
    print(f'#{test_case} {cnt}')
