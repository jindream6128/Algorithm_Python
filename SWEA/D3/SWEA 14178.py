import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N ,D =map(int, input().split())
    x = 2*D+1
    if N % x == 0:
        num = N//x
    else:
        num = N//x + 1

    print(f'#{tc} {num}')