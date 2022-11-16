import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, K =map(int, input().split())
    lstN = list(map(int,input().split()))
    lstN = sorted(lstN, reverse=True) #sorted로 리스트reverse 하는거조심
    ans = []
    for i in range(K):
        ans.append(lstN[i])

    print(f'#{tc} {sum(ans)}')