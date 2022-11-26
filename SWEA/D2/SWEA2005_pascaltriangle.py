T = int(input())
for test_case in  range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1) for a in range(N+1)]
    
    arr[1][1]=1
    for i in range(2, N+1):
        for j in range(1, i+1):
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j] #각 arr[i][j]값 저장하기
            
    print("#{}".format(test_case))#출력 양식 맞춰주기
    for i in range(1,N+1):
        for j in range(1,i+1): 
            print(arr[i][j], end=" ")#j가 한번돌고
        print("") #i가 한번더 늘어날때에는 한줄다음에 출력
    
    #j가 순환을 돌때 j에 끝 범위가N+1이 아니라, i+1이여야 한다 만약 N+1이라면 0이 출력이 되고 i+1이여야 아무것도 출력되지 않는다.