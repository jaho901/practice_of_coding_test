
## 10818
# 최소, 최대
'''
def solution(n, number):
    n = int(n)
    number = list(map(int, number.split()))

    maximum = max(number)
    minimum = min(number)

    print(minimum, maximum, end=" ")

a = input()
b = input()
solution(a, b)
'''

## 2562
# 최댓값
'''
number = []
for i in range(0,9):
    a = int(input())
    number.append(a)

def solution(num):
    print(max(num))
    print(number.index(max(num))+1)

solution(number)
'''

## 2577
# 숫자의 개수
'''
def solution(a, b, c):
    result = str(a * b * c)
    num = [0] * 10
    for i in range(len(result)):
        num[int(result[i])] += 1
    for i in num:
        print(i)

a = int(input())
b = int(input())
c = int(input())

solution(a, b, c)
'''

## 3052
# 나머지
'''
number = []
for i in range(0,10):
    a = int(input())
    number.append(a)
    

def solution(num):
    result = []
    for i in range(len(num)):
        result.append(num[i] % 42)
    result = set(result)
    length = len(result)
    print(length)

solution(number)
'''

## 1546
# 나머지
'''
n = int(input())
number = list(map(int, input().split()))

def solution(n, number):
    result = []
    maximum = max(number)
    for i in number:
        result.append((i/maximum)*100)
    print(sum(result)/n)


solution(n, number)
'''

## 8958
# OX 퀴즈
'''
T = int(input())
for tc in range(1, T+1):
    char = input()
    ans = []
    
    if char[0] == 'O':
        ans.append(1)
        result = 1
        for i in range(0, len(char)-1):
            if char[i+1] == 'O':
                result += 1
            else:
                result = 0
            ans.append(result)

    else:
        ans.append(0)
        result = 0
        for i in range(0, len(char)-1):
            if char[i+1] == 'O':
                result += 1
            else:
                result = 0
            ans.append(result)

    print(sum(ans))
'''
''' 스플릿으로 풀어보기
a = 'OOXXOXXOOO'.split('X')

a = list(a)
for i in a:
    if i == '':
        a.remove(i)
print(a)

result = []
sum = 0

for i in a:
    sum = 0
    for j in range(len(i)):
        sum += (j+1)
    result.append(sum)

print(result)
'''

## 4344
# 평균은 넘겠지

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    score = data[1:]
    avg = sum(score)/len(score)
    upper = 0
    lower = 0

    for i in score:
        if i > avg:
            upper += 1
        else:
            lower == 1
    result = upper/len(score)*100
    print('{0:.3f}%'.format(result))









