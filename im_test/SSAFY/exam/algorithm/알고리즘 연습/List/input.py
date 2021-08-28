import sys
sys.stdin = open('input.txt')

# 2개 받아오기
x, y = map(int, input().split())
print(x, y)


# 한 줄에 여러개의 숫자 값들을 받기
# 1. 리스트에 정수형으로 받기
list_1 = list(map(int, input().split()))
print(list_1)
# 2. 리스트에 문자열로 받기
list_2 = input().split()
print(list_2)
# 3. 문자열로 받기
str_1 = ''.join(input().split())
print(str_1)


# 콤마가 있는 상황에서 하나의 리스트로 들고오기
list_3 = list(map(int, input().split(', ')))
print(list_3)


# 3행 2열 들고오기
arr_1 = [list(map(int, input().split())) for _ in range(3)]
print(arr_1)


# 4행 2열 들고오기(콤마로 구분)
arr_2 = [list(map(int, input().split(', '))) for _ in range(4)]
print(arr_2)







