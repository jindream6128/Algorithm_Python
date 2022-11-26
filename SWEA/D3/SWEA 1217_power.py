# file input
# import sys
# sys.stdin = open("input.txt", "r")
def power(a,b):
    ans = 1
    for _ in range(b):
        ans *= a
    return ans

for tc in range(1,11):
    _ = input()
    a,b = map(int,input().split())
    print(f'#{tc} {power(a,b)}')
