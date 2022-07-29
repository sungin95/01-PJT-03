import sys

sys.stdin = open("_최빈수구하기.txt", "r")

t = int(input())
for test_case in range(1, t + 1):
    ___ = int(input())
    N = map(int, input().split())
    score_dict = {}
    for i in N:
        if score_dict.get(i) == None: # 딕셔너리를 만들어 카운트(키 점수, 밸류 등장 횟수)
            score_dict[i] = 1
        else: 
            score_dict[i] += 1

    most_frequent = 0 # 등장 횟수
    mf_score = 0 # 정답
    for j in range(101): # 등장 횟수가 가장 많은 횟수(밸류)를 알아낸 다음에 그 점수(키)를 알아낸다. 같으면 가장 높은 점수를 알아야 하니까 레인쥐
        if score_dict.get(j) != None: # 크거나 같음을 사용하여 횟수가 같을때는 더 큰 점수로 기록.
            if score_dict[j] >= most_frequent:
                most_frequent = score_dict[j]
                mf_score = j

                
    print(f"#{test_case} {mf_score}")