
## no_10952
# A + B - 5
'''
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
'''

## no_10951
# A + B - 4
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
'''


## no_1110
# 더하기 사이클
'''
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)
'''












