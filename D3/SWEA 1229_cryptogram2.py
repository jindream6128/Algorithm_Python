import sys
sys.stdin = open("input.txt", "r")
for tc in range(1,11):
    N = int(input()) #원본 암호문 길이
    crypto = list(input().split()) #원본 암호문
    M = int(input()) #명령어의 갯수
    command = list(input().split()) #명령어
    for i in range(len(command)):
        if command[i] == 'I':
            idx = int(command[i+1])
            num = int(command[i+2])
            for j in range(num):
                crypto.insert(idx+j, command[i+2+j+1])
        elif command[i] == 'D':
            idx = int(command[i+1])
            num = int(command[i+2])
            # for j in range(num):
            #     crypto.pop(idx+j)

            for _ in range(num):
                del crypto[idx]
        else:
            continue

    ans = []
    for k in range(10):
        ans.append(crypto[k])
    print(f'#{tc}', *ans)
