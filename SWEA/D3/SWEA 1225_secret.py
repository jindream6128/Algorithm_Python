import sys
sys.stdin = open("input.txt", "r")

# 큐 자료구조
def password(list):
    while True:
        for i in range(1,6): #
            num = list.pop(0)
            list.append(num - i)

            if list[7] <= 0:
                list[7] = 0
                return list


for tc in range(1,11):
    _ = input()
    lst = list(map(int,input().split()))

    result = password(lst)
    print(f'#{tc}', *result)
