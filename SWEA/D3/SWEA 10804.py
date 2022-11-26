import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1,T+1):
    s = list(input())
    s= s[::-1]
    for j in range(0, len(s)):
        if s[j] == 'b':
            s[j] = 'd'
        elif s[j] == 'd':
            s[j] = 'b'
        elif s[j] == 'q':
            s[j] = 'p'
        elif s[j] == 'p':
            s[j] ='q'

    print(f'#{tc} ', *s, sep ="")