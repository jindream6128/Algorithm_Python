import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # ans = []
    # for i in range(1,10):
    #     for j in range(1,10):
    #         ans.append(i*j)
    #
    # if N in ans:
    #     print(f'#{tc} Yes')
    # else:
    #     print(f'#{tc} No')
    ans = 'No'
    for i in range(1,10):
        if N % i == 0 and (N//i)<=9:
            ans = 'Yes'
            break
    print(f'#{tc} {ans}')



