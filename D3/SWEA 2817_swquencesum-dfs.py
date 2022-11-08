# file input
import sys
sys.stdin = open("input.txt", "r")
# from itertools import combinations
def dfs(n, sm):#n은 index이다
    global cnt
    if K < sm: #가지치기 sm값이 K보다 넘어가면 더이상 할필요 없음
        return
    if n==N:# 마지막 까지 다 하였을때 종료
        if sm == K: #sm값과 K가 같아지면 1회 cnt가 추가된다.
            cnt += 1
        return

    else:
        dfs(n+1, sm+lst[n]) #다음 원소를 사용할 경우에는 sm값에 누적으로 합을 해준다
        dfs(n+1, sm) #다음 원소를 사용하지 않을 경우에는 sm값에 더하지 않는다.

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)

    print(f'#{tc} {cnt}')