import sys
sys.stdin = open("input.txt", "r")

def dfs(index, score, cal):
    global best_score
    if cal > L:
        return
    if score> best_score: #best_score가 더 작으면 score가 best_score가 된다
        best_score = score
    if index == N:
        return
    dfs(index +1, score+lst[index][0], cal +lst[index][1]) #재료 사용
    dfs(index+1, score, cal) #사용 X

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    lst = []
    best_score = 0
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    dfs(0,0,0)
    print(f'#{tc} {best_score}')