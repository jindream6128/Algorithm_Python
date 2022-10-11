T = int(input())
for test_case in range(1,T+1):
    sum1=0
    sum2=0
    N=int(input())
    for i in range(1, N+1):
        if (i%2)==1:
            sum1 += i #홀수의합
        elif (i%2)==0:
            sum2 += i #짝수의합
        ans = sum1 - sum2
        
    print("#{} {}".format(test_case, ans))