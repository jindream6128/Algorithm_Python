# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N =int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    ans=0
    M= N//2

    for i in range(0, N):
        if i<=M:
            for j in range(M-i,M+i+1):
                ans += arr[i][j]
        else:
            for j in range(i-M,N-(i-M)):
                ans += arr[i][j]

    print(f'#{test_case} {ans}')