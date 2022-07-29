# 처음 봤을때는 밸붕 문제라고 생각했는데. 다행히 문제를 이해하는데 성공해 풀 수 있었습니다. 
# 문제가 어려워 보이지만 결국에는 insert문제 였습니다. x위치에 암호를 넣어주는 문제였습니다. 
import sys

sys.stdin = open("_암호문1.txt", "r")

t = 10
for test_case in range(1, t + 1):
    _ = input()
    answer = ""
    first = list(map(int, input().split()))

    insert_n = int(input())

    xys_all = input().split('I') # I를 기준으로 나누면 좋겠다고 생각했습니다. 

    for j in range(1,insert_n+1): # I기준이다 보니 맨 앞은 빼 주기 위해 시작점 1로 했습니다. 
        xys = list(reversed(list(map(int, xys_all[j].split())))) # 처음값이 앞에 오기 위해 reversed를 주었습니다. 
        for i in range(xys[-2]): # xys[-2] 가 y 문자 갯수입니다
            first.insert(xys[-1], xys[i]) # xys[-1] 가 x 문자 넣어야 하는 위치 입니다. xys[i]가 s 암호입니다. 
    for i in range(10):
        answer += f"{str(first[i])} "
    print(f"#{test_case} {answer}")

    


