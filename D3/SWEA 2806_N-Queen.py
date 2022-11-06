# file input
# import sys
# sys.stdin = open("input.txt", "r")

def dfs(i):
    global ans #여기서는 dfs가 정상적으로 한번 돌아야 퀸이 들어갈 자리가 있는거므로 정상적으로 돌고 난 뒤 ans값에 1을 더한다
    if i == N: #시작0열 부터 마지막 열까지 돈다면 멈춘다
        ans += 1
        return
    for j in range(0, N):
        if v1[j] == v2[i+j] == v3[i-j] == 0: #같은 행에 있는지, 각 대각선 방면으로 존재하는게 있는지 확인하고, 없다면 반복된다.
            v1[j]=v2[i+j]=v3[i-j]=1 #1을 추가해주고
            dfs(i+1) #재귀를 호출한다
            v1[j]=v2[i+j]=v3[i-j]=0 #다시 방문을 0으로 바꿔준다



T = int(input())
for test_case in range(1, T+1):
    N =int(input())
    ans = 0

    v1,v2,v3 = [[0]*(2*N) for _ in range(3)] # 같은 행에 퀸이 있는지 확인하기, v2는 오른쪽 위의 방향으로 퀸이 있는지, v3는 오른쪽 아래 방향으로 퀸이 있는지의 여부를 확인하기 위함
    dfs(0)
    print(f'#{test_case} {ans}')