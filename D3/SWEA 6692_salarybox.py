import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans =[]
    for _ in range(N):
        c = list(map(float, input().split()))
        ans.append(c[0]*c[1])

    print(f'#{tc} {sum(ans):.6f}') #f-string에서 소수점아래 6자리 출력하는 방법 외우기