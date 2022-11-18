import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    p,q = map(int, input().split())
    #100X100
    arr = []
    for k in range(2, 201):
        for i in range(1,101):
            for j in range(1, 101):
                if i+j == k:
                    arr[i][j].append(k)

    print(arr)
