import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string=list(input())
    a,b=1,1
    for i in range(len(string)):
        if string[i] =='L':
            b=a+b
        if string[i] == 'R':
            a=a+b

    print(f'#{tc} {a} {b}')
