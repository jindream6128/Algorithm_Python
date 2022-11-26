import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a=2*M-N
    b=N-M
    print(f'#{tc} {a} {b}')