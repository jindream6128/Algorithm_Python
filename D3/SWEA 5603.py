import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [int(input()) for _ in range(N)] #건초 더미 lst로 받기
    av = sum(lst) // N
    ans = []
    result=0
    for i in range(len(lst)):
        ans.append(av - lst[i])

    for j in range(len(ans)):
        if 0 < ans[j]:
            result += ans[j]
    print(f'#{tc} {result}')
