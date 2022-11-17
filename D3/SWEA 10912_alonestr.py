import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    slst = list(set(lst))
    ans = []

    for i in range (len(slst)): 
        if (lst.count(slst[i])) % 2 != 0: #집합으로 만들어서 중복은 없다.거기서 count해서 1개짜리는 append 해주고 2개짜리는 그대로둔다
            ans.append(slst[i]) #1개 짜리만 저장되는 list
        else:
            continue
    ans.sort() #오름차순 정렬
    result = ''.join(ans) #문제 출력 맞춰서 출력하기위해 result에 join하기
    if len(ans) == 0:
        print(f'#{tc} Good')
    else:
        print(f'#{tc} {result}')