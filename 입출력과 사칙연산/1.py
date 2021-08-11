
# a / b
'''
a, b = map(int, input().split())

print(a/b)
'''

# 두 수 비교
'''
a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
'''

# 손익 분기점

a = int(input())
b = input()
c = list(map(int, b))
result = []
for i in range(-1, -(len(c)+1), -1):
    result.append(a * c[i])
result.append(a * int(b))
for i in result:
    print(i)






















