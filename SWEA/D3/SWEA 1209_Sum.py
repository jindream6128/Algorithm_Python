# file input
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N =int(input())
    arr = [list(map(int, input().split())) for _ in range (100)]
    sum_arr = []
    ans1, ans2 = 0,0

    for i in range(0,100): #오른쪽 아래 대각선
        ans1 += arr[i][i]
        sum_arr.append(ans1)

    for i in range(0,100): #왼쪽 아래 대각선
        ans2 += arr[i][-(i+1)+100]
        sum_arr.append(ans2)

    for i in range(0,100):
        #가로 합
        ans = sum([arr[i][j] for j in range(0,100)])
        sum_arr.append(ans)
        #세로 합
        ans = sum([arr[j][i] for j in range(0,100)])
        sum_arr.append(ans)

    print(f'#{N} {max(sum_arr)}')
