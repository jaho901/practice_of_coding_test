## 11720 
# 숫자의 합
'''
N = int(input())
num = list(input())
result = 0

for i in num:
    result += int(i)

print(result)
'''

## 10809
# 알파벳 찾기
'''
string = list(input())
# print(string)
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
# print(alphabet)

result = [0] * 26

for i in range(len(alphabet)):
    if alphabet[i] in string:
        if result[i] == True:
            pass
        else:
            idx = string.index(alphabet[i])
            result[i] = idx
    else:
        result[i] = -1
    
print(*result)
'''

## 2675
# 문자열 반복
'''
T = int(input())
for i in range(1, T+1):
    N, alpha = input().split()
    N = int(N)
    alpha = list(alpha)
    result = []
    
    for i in alpha:
        for j in range(N):
            result.append(i)

    result = ''.join(result)
    print(result)
'''

## 1157
# 단어 공부
'''
string = input()
string_lo = list(string.lower())
string_unique = list(set(string_lo))
string_unique = sorted(string_unique)

length = len(string_unique)
result = [0] * length

for i in range(length):
    cnt = string_lo.count(string_unique[i])
    result[i] += cnt

maximum = max(result)

if result.count(maximum) > 1:
    print('?')

else:
    idx = result.index(maximum)
    print(string_unique[idx].upper())
'''

## 1152
# 단어의 개수
'''
string = input()
space = string.count(' ')
length = len(string)
if string[0] == ' ':
    space -= 1
if string[length-1] == ' ':
    space -= 1

print(space + 1)
'''

## 2908
# 상수
'''
a, b = input().split()

new_a, new_b = '', ''

# new_a, new_b에 앞뒤 바꿔서 넣기
for i in range(len(a)-1, -1, -1):
    new_a += a[i]
for j in range(len(b)-1, -1, -1):
    new_b += b[j]

if new_a > new_b:
    print(new_a)
else:
    print(new_b)
'''


## 5622
# 다이얼
'''
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i).upper())

number = [2]*3 + [3]*3 + [4]*3 + [5]*3 + [6]*3 + [7]*4 + [8]*3 + [9]*4

string = list(input())

result = 0

for i in string:
    idx = alphabet.index(i)
    result += number[idx] + 1

print(result)
'''
'''
alphabet = ['0', '0', '0', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
result = 0
for i in word:
    for j in range(len(alphabet)):
        if i in alphabet[j]:
            result += j
print(result)
'''


## 2941
# 크로아티아 알파벳
'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

result = 0

for i in croatia:
    while i in string:
        string = string.replace(i, '*', 1)
        result += 1

cnt = string.count('*')
result += len(string)
result -= cnt

print(result)
'''

## 1316
# 그룹 단어 체커

N = int(input())
result = 0
for i in range(1, N+1):
    string = input()
    unique = string[0]
    for i in range(1, len(string)):
        if unique[-1] == string[i]:
            pass
        elif unique[-1] != string[i]:
            unique += string[i]
    # print(unique)

    cnt = 0
    for i in unique:
        if unique.count(i) == 1:
            cnt += 1
    if cnt == len(unique):
        result += 1

print(result)













