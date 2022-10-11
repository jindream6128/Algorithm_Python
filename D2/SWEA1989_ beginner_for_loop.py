T = int(input())
for test_case in range(1,T+1):
    string = input()
    reverse_string = string[::-1] #문자열 뒤집기
    
    if string == reverse_string:
        print("#{} 1".format(test_case))
        
    else:
        print("#{} 0".format(test_case))
        