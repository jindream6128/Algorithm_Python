import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    N = int(input()) #원본 암호문의 길이 N
    crypto = list(input().split()) #원본 암호문
    M = int(input()) #명렁어의 갯수
    command = list(input().split()) #명렁어
    # I 인설트 해라 x의 위치 바로 다음에 y개의 숫자를 삽입
    for i in range(len(command)):
        if command[i] == 'I':
            idx = int(command[i+1])
            num = int(command[i+2])
            for j in range(num):
                crypto.insert(idx+j, int(command[i+2+j+1]))
        else:
            continue
    ans = []
    for a in range(0,10):
        ans.append(crypto[a])

    print(f'#{tc}',*ans)