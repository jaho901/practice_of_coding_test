import sys
sys.stdin = open('1439.txt')

num = list(map(int,input()))
result = []
for i in range(len(num)-1):
    if num[i] == num[i+1]:
        continue
    else:
        result.append(num[i])
result.append(num[-1])
a = result.count(0)
b = result.count(1)
if a < b:
    print(a)
elif a > b:
    print(b)
else:
    print(a)