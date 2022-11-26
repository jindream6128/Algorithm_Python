import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split()) # 총 수강생N 과제제출한 사람의 수 K
    lst_k = list(map(int, input().split())) # 과제를 제출한 사람의 번호 1번부터
    lst_N =[]
    for i in range(1,N+1):
        lst_N.append(i)

    for j in lst_k:
        lst_N.remove(j)

    print(f'#{tc}', *lst_N)