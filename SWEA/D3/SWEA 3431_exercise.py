# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    if U < X :
        print(f'#{test_case} {-1}')
    elif L <= X <= U:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {L-X}')