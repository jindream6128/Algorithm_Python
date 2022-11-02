# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
ans = 0
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    for _ in range(b):
        ans *= a
    print(f'#{test_case} {ans}')
