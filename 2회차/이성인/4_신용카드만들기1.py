import sys

sys.stdin = open("_신용카드만들기1.txt", "r")

t = int(input())
for test_case in range(1, t + 1):
    odd_number = 0
    even_number = 0
    answer = 0
    a,b,c,d,e,f,g,h,i,j,k,l,n,m,o = map(int, input().split()) # 15개까지는 노가다가 더 편할거 같아서요ㅎㅎ
    odd_number = ( a + c + e + g + i + k + n + o)*2 # 홀수 값 합 * 2
    even_number = ( b + d + f + h + j + l + m) # 짝수값 합
    N = odd_number + even_number
    answer = (10 -(N % 10)) % 10 # 합이 0일때를 위해 % 10을 마지막에 추가 했습니다. 

    print(f"#{test_case} {answer}")