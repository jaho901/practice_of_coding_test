# a + b - 2
'''
def plus(a, b):
    return a+b

a = int(input())
b = int(input())

print(plus(a, b))
'''

# party
'''
def party(n, p, num):
    total = n * p
    for i in num:
        print(i-total, end=" ")

n, p = map(int, input().split())
num = list(map(int, input().split()))

party(n, p, num)
'''

# copyright
'''
def solution(a):
    a = list(map(int, a.split()))
    result = a[0] * (a[1] - 1)
    return result + 1

a = input()
print(solution(a))
'''


# chess
'''
def solution(a):
    # 완성본
    perfect = [1, 1, 2, 2, 2, 8]
    b = list(map(int, a.split()))
    # 최종 결과물
    result = []
    for i in range(len(perfect)):
        result.append(perfect[i]-b[i])
    return result

a = input()
# 리스트안에 있는 요소를 공백으로 꺼내주는 역할 = 리스트 앞에 '*' 붙이기
print(*solution(a))
'''


# R2

def solution(num):
    a, avg = map(int, num.split())
    result = avg * 2
    return result - a

a = input()
print(solution(a))



















