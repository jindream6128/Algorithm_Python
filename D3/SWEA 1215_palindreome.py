# file input
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())  # 찾아야하는 회문의 길이 N
    arr = [list(input()) for _ in range(8)]  # 단어 입력 8*8
    ans = 0

    for i in range(0,8): #가로 회문
        for j in range(0,8-N+1):
            ans1 = arr[i][j:j+N]
            ans2=ans1[::-1]
            if ans1 == ans2:
                ans +=1

    for j in range(0,8): #세로 회문
        for i in range(0,8-N+1):
            ans3 =''
            for k in range(i,i+N):
                ans3 += arr[k][j]
            ans4 = ans3[::-1]
            if ans3 == ans4:
                    ans+=1

    print(f'#{tc} {ans}')
