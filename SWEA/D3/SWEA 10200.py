import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    mx = min(A,B)
    if A+B > N:
        mi = A+B-N
    else:
        mi =0
    print(f'#{tc} {mx} {mi}')