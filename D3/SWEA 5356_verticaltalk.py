import sys
sys.stdin = open("input.txt", "r")
# 다시보기
T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    ln = []
    ans = ''
    for i in arr:
        ln.append(len(i))

    for a in range(0, max(ln)):
        for b in range(5):
            if a < ln[b]:
                ans += arr[b][a]

    print(f'#{tc} {ans}')