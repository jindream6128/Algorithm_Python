T = int(input())
for test_case in range(1,T+1):
    arr = list(map(int,input().split()))
    
    hour = arr[0]+arr[2]
    min = arr[1]+arr[3]
    
    if min > 59:
        hour = hour +1
        min = min - 60
        
    if hour > 12:
        hour = hour - 12
            
    print("#{} {} {}".format(test_case, hour, min))
