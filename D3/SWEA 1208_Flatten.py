# file input
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):

    N = int(input())
    lst = list(map(int, input().split()))

    for _ in range(N): #덤프 즉 바꾸는 횟수만큼 반복한다.
        #인덱스를 통해서 값에 접근해야 리스트의 값이 바뀐다
        maxindex = lst.index(max(lst)) #max값의 인덱스를 maxindex에 저장한다
        minindex = lst.index(min(lst)) #min값의 인덱스를 minindex에 저장한다
        lst[maxindex] -= 1 #max값에는 1빼고
        lst[minindex] += 1 #min값에는 1을 더한다

    ans = max(lst)-min(lst) #정답은 최고점과 최저점의 높이차

    print(f'#{tc} {ans}')