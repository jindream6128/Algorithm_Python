import sys
sys.stdin = open("input.txt", "r")
import itertools

T = int (input())
for tc in range(1,T+1):
    lst = list( input().split())
    ans = itertools.combinations(lst,3)

    print(list(ans))
