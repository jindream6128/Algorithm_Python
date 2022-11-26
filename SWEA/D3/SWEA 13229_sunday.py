import sys
sys.stdin = open("input.txt", "r")
dic = {'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6, 'SUN':7}

T = int(input())
for tc in range(1, T+1):
    w=input()
    ans = 7 - dic[w]
    if ans == 0:
        ans = 7
    print(f'#{tc} {ans}')