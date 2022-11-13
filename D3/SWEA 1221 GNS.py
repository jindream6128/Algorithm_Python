# file input
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    _, num = input().split()
    lst = list(input().split())

    lst_str=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    lst_num = [0]*len(lst_str)

    for number in lst:
        for i in range(0,10):
            if number == lst_str[i]:
                lst_num[i] += 1
                break

    ans = []
    for a in range(len(lst_str)):
        ans.append(' '.join( lst_str[a] for _ in range(lst_num[a])))

    result = ' '.join(ans)

    print(f'#{tc}')
    print(f'{result}')
    # print(*ans, sep=' ')