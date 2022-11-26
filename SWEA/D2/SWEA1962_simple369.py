T = int(input())
cnt = 0

for i in range(1, T+1):
    li = str(i) #문자열로 저장해야 정상동작, list로 저장하니 각자리를 리스트로 저장하여 동작
    cnt = li.count('3')+li.count('6')+li.count('9') #문자열 중에 3,6,9가 들어가는 경우를 cnt
    
    if cnt ==0: #3,6,9가 들어가지 않는 경우이므로 정상 문자열 출력
        print(li, end = " ")
        
    else: #cnt만큼 -를 출력한다
        print("-"*cnt, end=" ")