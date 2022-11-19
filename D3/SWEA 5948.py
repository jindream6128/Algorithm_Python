import itertools
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    lst = list(map(int, input().split()))
    ans = itertools.combinations(lst,3)
    ans = list(ans)
    result = []
    for i in range(0, len(ans)):
        result.append(sum(ans[i]))
    result = list(set(result))
    result.sort(reverse=True)
    print(f'#{tc} {result[4]}')