import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1,T+1):
    num = int(input())
    if num %2 ==0 :
        print(f'#{tc} Alice')
    else:
        print(f'#{tc} Bob')