import sys

sys.stdin = open("_신용카드만들기2.txt", "r")

t = int(input())
for test_case in range(1, t + 1):
    N = input()
    make_card_able = 1
    if N[0] == "3" or N[0] == "4" or N[0] == "5" or N[0] == "6" or N[0] == "9": # 생각해 보니 if N[0] in ['3', '4', '5', '6', '9' ]가 더 편했을거 같네요. 
        make_card_able = 1
    else:
        make_card_able = 0

    n_ = N.count("-")

    n = len(N)
    if n - n_ != 16: # - 갯수를 카운터해 전체 길이에서 빼 주었습니다. 
        make_card_able = 0

    print(f"#{test_case} {make_card_able}")