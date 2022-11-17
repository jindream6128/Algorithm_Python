import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    ln = int(input())
    word = list(input().split())
    ans = []

    if len(word) % 2 ==0:
        for i in range(0, ln//2):
            ans.append(word[i])
            ans.append(word[i+ln//2])
    elif len(word) %2 == 1:
        for j in range(0, (ln//2)):
            ans. append(word[j])
            ans.append(word[j+(ln//2)+1])
        ans.append(word[ln//2])
    result = ' '.join(ans)
    print(f'#{tc} {result}')