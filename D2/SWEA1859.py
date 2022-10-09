T = int(input())
for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int,input().split()))[::-1] #입력받은 배열을 거꿀로 만들어준다
    sum = max = 0 #최대값은 0으로, 합도 0으로 선언한다
    
    for j in N_list: #N_list만큼 반복을 돌린다 (index가 아닌 value)
        if max<=j: #max값이 다음 원소보다 작거나 같으면 max값을 그 원소로 교체해준다 
            max = j
        else: #max값이 여전히 최대값이라면 max-N_list(j)의 값을 sum에 저장한다.
            sum += (max-j)
            
    print("#{} {}".format(i, sum))
 