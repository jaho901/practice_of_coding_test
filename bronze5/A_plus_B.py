def plus(a, b):
    result = a + b
    return result

# a = list(map(int, input().split()))

a1, a2 = map(int, input().split())
print(plus(a1, a2))

#str형으로 입력받고싶어
a = input()  

# int형으로 입력받고싶어
a = int(input())

# 1 2 3 4 여러개를 공백으로 구분해서 입력받고싶어
a = input().split()

# split은 리스트로 반환해줘
a = ['1','2','3','4']  

# int로 바꿔주고싶어
a = list(map(int,input().split()))  

# 변수 여러개에 따로따로 입력을 저장하고싶어
a, b = input().split()  

# a = '1', b= '2'  # 변수 여러개에 따로따로 int로 받고싶어 
a, b = map(int, input().split()) # a = 1 , b = 2