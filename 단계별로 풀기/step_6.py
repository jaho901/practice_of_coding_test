
## 15596
# 정수 N개의 합
'''
def solve(number):
    result = 0
    for i in number:
        result += i
    return result

n = input()
print(solve(n))
'''

## 4673
# 셀프 넘버
'''
na_num = set(range(1, 10001))
ge_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    ge_num.add(i)

self_num = sorted(na_num - ge_num)
for i in self_num:
    print(i)
'''

## 1065
# 한수

n = input()
num = int(n)
result = 99

if len(n) <= 2:
    result = n

elif len(n) <= 4:
    while num >= 100:
        if int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]):
            result += 1
        num -= 1
        n = str(int(n)-1)

print(result)











