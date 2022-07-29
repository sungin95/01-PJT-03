import sys

sys.stdin = open("_문자열의거울상.txt" ,"r")

str_dict = {
    'b': 'd',
    'd': 'b',
    'q': 'p',
    'p': 'q'
}

t = int(input())
for test_case in range(1, t + 1): # 이 문제는 딕셔너리를 이용하여 입력을 키로 받으면 밸류를 반대대는 문자로 주었습니다. 
    str_ =  input()
    revers_str = ""
    for i in str_:
        revers_str =  str_dict[i] + revers_str # 문자 거꾸로 만드는 식 타키썜이 알려준거 너무 유용해 ㅎㅎ
    print(f"#{test_case} {revers_str}")


