# file input
# import sys
# sys.stdin = open("input.txt", "r")

for tc in range(1,11):

    N = int(input())
    lst = list(map(int, input().split()))
    for _ in range(N):
        ma = lst.index(max(lst))
        mi = lst.index(min(lst))
        lst[ma] -= 1
        lst[mi] += 1

    ans = max(lst)-min(lst)

    print(f'#{tc} {ans}')