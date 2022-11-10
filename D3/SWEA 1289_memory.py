# file input
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input()))
    cnt = 0
    lst =[0] * len(num) #0000 num의 길이만큼0을 만들어 준다

    for i in range(0, len(num)):
        if num[i] != lst[i]: #num과 lst의 각 자리별로 원소를 비교해서 동일하지 않을때 숫자를 바꿔준다
            cnt += 1 #동일하지 않은경우 숫자가 바뀌므로cnt가 +1이 되고 if, elif문을 사용해야한다. if if를 사용하면 첫번째 if이후 나온결과값이 두번째 if문을 도는거고, if elif를 사용하면 둘중에 만족하는 if문을 도는거다
            if lst[i] == 0: #만약 0이라면 그뒤에 숫자는 모두 1로 바꿔준다
                for j in range(i, len(num)):
                    lst[j] = 1
            elif lst[i] == 1: #만약 1이라면 그뒤에 숫자는 모두 0으로 바꿔준다.
                for j in range(i,len(num)):
                    lst[j] = 0
        else: #동일한 경우 다음자리를 check한다.
             continue
    print(f'#{test_case} {cnt}')

