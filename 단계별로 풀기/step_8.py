## 1712
# 손익분기점
'''
A, B, C = map(int, input().split())

if C > B:
    result = (A / (C - B)) + 1

else:
    result = -1

print(int(result))
'''


## 2292
# 벌집
'''
N = int(input())

i = 1
room = 1
num = 1

while num < N:
    num = num + 6*i
    room += 1
    i += 1

print(room)
'''

## 1193
# 분수 찾기
'''
num = int(input())
num1 = num
i = 1

while num > i:
    num -= i
    i += 1
# print(i)

nn = 0
for k in range(1, i):
    nn += k
# print(nn)

result = []
if i % 2 == 0:
    for j in range(1, i+1):
        a = str(j) + '/' + str(i+1-j)
        result.append(a)
else:
    for j in range(1, i+1):
        a = str(i+1-j) + '/' + str(j)
        result.append(a)

print(result[num1-nn-1])
'''

## 2869
# 달팽이는 올라가고 싶다.
'''
A, B, V = map(int, input().split())

result = (V-A)/(A-B) + 1
if result - int(result) > 0:
    result = int(result) + 1
else:
    result = int(result)
print(result)
'''

## 10250
# ACM 호텔
'''
T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    result = []

    w = N // H + 1
    h = N % H
    
    if w < 10:
        result = '{0}0{1}'.format(h, w)
    else:
        result = '{0}{1}'.format(h, w)
    print(result)
'''

    '''
    for w in range(1, W+1):
        for h in range(1, H+1):
            result.append((w, h))
            N -= 1
            if N == 0:
                break
        if N == 0:
            break

    w = result[-1][0]
    h = result[-1][1]
    
    if w < 10:
        result = '{0}0{1}'.format(h, w)
    else:
        result = '{0}{1}'.format(h, w)
    print(result)
    '''




