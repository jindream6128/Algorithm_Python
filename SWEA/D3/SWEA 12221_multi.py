import sys
sys.stdin = open("input.txt", "r")
def mul(A,B):
    if A<10 and B<10:
        return A*B
    else:
        return -1

T = int(input())
for tc in range(1,T+1):
    A, B = map(int, input().split())
    print(f'#{tc} {mul(A,B)}')
