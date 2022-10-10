T = int(input())
for i in range(1, T+1):
    
    text = input()
    pattern = []
    pattern_2 = []
    result =0
    
    for j in range(1, 11): #문제에 패턴은 10까지만이기 때문에 10까지만 반복을 돌아준다.
        pattern = text[:j] 
        pattern_2 = text[j:j*2]
        if pattern == pattern_2: #패턴과 패턴2가 동일해진다면
            result = len(pattern) #패턴의 길이를 저장하고
            break #더이상의 반복을 멈춘다.
            
    print("#{} {}".format(i, result))