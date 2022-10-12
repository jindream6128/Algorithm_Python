grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] #성적은 미리 list로 저장 -> 문자열 저장 따음표 !

T = int(input())
for test_case in range(1,T+1):
    ans_list= [] #총점을 저장할 리스트 만들기
    N, K = map(int, input().split())
    for i in range(N):
        mid, final, hom = map(int, input().split())
        ans = (mid*0.35)+(final*0.45)+(hom*0.2)
        ans_list.append(ans) #ans_list에 ans값을 넣는다
    
    #정렬전에 K번째 학생의 총점을 저장해야 한다
    k_ans = ans_list[K-1]
    ans_list.sort(reverse=True) #내림차순 정리

    overlap = N//10 #동일한 등급은 N/10의 학생이 가질수 있다.
    result = ans_list.index(k_ans)//overlap #K번째 학생의 index에다가 나눈몫은 0 1 2 3 grade와 동일해진다
    
    print("#{} {}".format(test_case, grade[result]))
    