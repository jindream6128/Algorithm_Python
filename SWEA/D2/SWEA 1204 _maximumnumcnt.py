from collections import Counter

def modefinder(numbers):
    c = Counter(numbers) #횟수 세기
    order = c.most_common() #나온 횟수가 최댓값 부터 내림차순으로 정렬
    maximum = order [0][0] #그중에서 첫번째 값(가장 많이 나온 문자)의 횟수를 maximum 에 저장
    
    # 여기는 정렬되 key 들의 리스트를 만드는것.
    # 결국 정렬된 Key들의 리스트를 만들어서 append 해준다.
    # modes= [] #빈 리스트 만들기
    # for num in order: #num은 각 문자의 빈도수 만큼 반복한다
    #     if num[1]==maximum:  
    #         modes.append(num[0])
    return maximum

T=int(input())
for test_case in range(1, T+1):
    case = int(input())
    grade = list(map(int,input().split()))
    ans = modefinder(grade)
    print(f'#{case} {ans}')