N = int(input())
measure = [] #약수 저장할 리스트
for i in range (1,N+1):
    if (N%i) == 0:
        measure.append(i) #i가 1 부터 돌아가기 때문에 오름차순으로 들어가진다
    else:
        None #나머지가 있는값은 버리기
print(*measure) #output처럼 출력하기위해