import sys
sys.stdin = open("input.txt", "r")

pw = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for lst in arr:
        if '1' in lst:
            last = M-1
            while lst[last] == '0':
                last -=1

            ans =[]
            for i in range(last-55,last+1,7):
                ans.append(pw[lst[i:i+7]])

            if (sum(ans[0:8:2])*3 + sum(ans[1:8:2]))%10 == 0:
                result = sum(ans[0:8:1])
            else:
                result =0

    print(f'#{tc} {result}')