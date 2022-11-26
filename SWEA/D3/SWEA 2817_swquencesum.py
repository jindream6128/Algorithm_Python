# file input
# import sys
# sys.stdin = open("input.txt", "r")
from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(1, N+1):
        for test in combinations(lst, i): #여기서 test에 각 경우의수를 조합한게 튜플로 나온다
            if sum(test) == K:
                cnt +=1

    print(f'#{tc} {cnt}')