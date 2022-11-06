# file input
# import sys
# sys.stdin = open("input.txt", "r")

def dfs(i):
    global ans
    if i == N:
        ans += 1
        return
    for j in range(0, N):
        if v1[j] == v2[i+j] == v3[i-j] == 0:
            v1[j]=v2[i+j]=v3[i-j]=1
            dfs(i+1)
            v1[j]=v2[i+j]=v3[i-j]=0



T = int(input())
for test_case in range(1, T+1):
    N =int(input())
    ans = 0

    v1,v2,v3 = [[0]*(2*N) for _ in range(3)]
    dfs(0)
    print(f'#{test_case} {ans}')