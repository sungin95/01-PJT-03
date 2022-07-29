import sys

sys.stdin = open("_소득불균형.txt", "r")

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    incomes = list(map(int, input().split())) # 소득 리스트화하여 for구문에 활용
    average = sum(incomes)//n # 소득은 정수로 주어졌다. 평균은 소수점 자리가 나오겠지만 몫만 구하여 그 값 이하는 평균 이하이다. 
    cnt = 0
    for i in incomes:
        if average >= i: # 평균이하 일때 마다 카운터 하였습니다. 
            cnt += 1
    print(f"#{test_case} {cnt}")

