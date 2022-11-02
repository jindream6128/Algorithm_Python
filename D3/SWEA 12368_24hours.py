# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    a,b = map(int, input().split())
    sum = a + b
    if sum >= 24:
        sum = sum-24
    print(f'#{test_case} {sum}')