
## no_2739
# 구구단
'''
n = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n*i))
'''

## no_10950
# A + B - 3
'''
T = int(input())

for i in range(1, T + 1):

    a, b = map(int, input().split())
    print(a + b)
'''


## no_15552
# 빠른 A + B
'''
import sys
T = int(input())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
'''


## no_2741
# N 찍기
'''
n = int(input())
i = 1
while i <= n:
    print(i)
    i += 1
'''


## no_2742
# 기찍 N
'''
n = int(input())
while n > 0:
    print(n)
    n -= 1
'''


## no_11021
# A + B - 7
'''
T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    result = a + b
    print('Case #{}: {}'.format(tc, result))
'''

## no_11022
# A + B - 8
'''
T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    result = a + b
    print('Case #{0}: {1} + {2} = {3}'.format(tc, a, b, result))
'''


## no_2438
# 별 찍기-1
'''
n = int(input())
for i in range(1, n+1):
    print('*' * i)
'''


## no_2439
# 별 찍기-2
'''
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
'''

## no_10871
# x보다 작은 수

N, X = map(int, input().split())

number = list(map(int, input().split()))
result = []
for i in number:
    if i < X:
        result.append(i)

print(*result)















