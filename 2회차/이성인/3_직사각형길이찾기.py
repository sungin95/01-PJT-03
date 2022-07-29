import sys

sys.stdin = open("_직사각형길이찾기.txt", "r")

t = int(input())
for test_case in range(1, t + 1): # 직사각형은 같은 길이의 변이 2쌍은 사각형입니다. 
    a, b, c = map(int, input().split())

    d = 0 
    if a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a

    print(f"#{test_case} {d}")