import sys
sys.stdin = open("input.txt", "r")

pw = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for lst in arr:
        last = M - 1
        if '1' in lst:
            while lst[last] == '0':
                last -= 1

            ans =[]
            # for i in range(8):
            #     ans.append(pw['lst[last-55:last+1][i*8:i*8+8]'])
            for i in range(last-55,last+1,7):
                ans.append(pw[lst[i:i+7]])

            check, check1, check2 =0,0,0
            for j in range(0,8,2):
                check1 += ans[j]
            for k in range(1,9,2):
                check2 += ans[k]
            check = (check1*3 + check2) % 10

            if check == 0:
                for a in range(0,8):
                    ansnum = 0
                    ansnum += ans[a]

    print(f'#{tc} {ansnum}')