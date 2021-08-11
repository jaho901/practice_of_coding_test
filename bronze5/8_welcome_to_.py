# welcome
'''
print(".  .   .")
print("|  | _ | _. _ ._ _  _")
print("|/\|(/.|(_.(_)[ | )(/.")
'''

# card_game
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
result = [a, b, c, d, e]
print(sum(result))
'''
'''
# 또 다른 방법
answer = 0
for i in range(5):
    answer += int(input())
print(answer)
'''

# 심부름 가는 길

# 1. home -> school
# 2. school -> pc
# 3. pc -> academy
# 4. academy -> home
# 60 < time < 3599
'''
answer = 0
for i in range(4):
    answer += int(input())

print(answer // 60)
print(answer % 60)
'''

# Next in line
'''
# 첫째와 둘째의 나이차와 둘째와 막내의 나이차가 동일하다.
# 둘째와 막내의 나이가 주어진다면 첫째의 나이는?

young = int(input())
middle = int(input())
diff = middle - young
first = middle + diff
print(first)
'''

# plane
'''
# n1 열은 k1 좌석들을 보유하고있고,
# n2 열은 k2 좌석들을 보유하고 있다.

# 총 좌석의 합은?

n1, k1, n2, k2 = map(int, input().split())
total = n1*k1 + n2*k2
print(total)
'''

# 팩토리얼
'''
n = int(input())
answer = 0
while n != 0:
    answer += n
    n -= 1
print(answer)

'''

# Julka
'''
summation = int(input())
Claudia = int(input())

Natalia = summation//2 - Claudia//2
Klauida = summation - Natalia

print(Klauida)
print(Natalia)
'''


# rest
'''
a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
'''

# today
'''
import datetime

print(str(datetime.datetime.now())[0:10])
'''

# we love kriii
'''
print('강한친구 대한육군')
print('강한친구 대한육군')
'''


# big number a+b
'''
a, b = map(int, input().split())
print(a + b)
'''

# 사칙 연산
'''
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
'''


# ??!
'''
a = input()
print(a + '??!')
'''

'''
a = "A"
print(ord(a))
'''


# 나는 행복합니다.
'''
N, M, K = map(int, input().split())
n = K // M
m = K % M
print(n, m)
'''

# 조별과제를 하려는데 조장이 사라졌다.

1 3 6 10 15

















