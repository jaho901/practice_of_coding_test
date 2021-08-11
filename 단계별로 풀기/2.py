## no_14681
# 사분면 고르기

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


## no_2753
# 윤년

def solution(n):
    if n % 4 == 0 and n % 100 != 0:
        print(1)
    elif n % 400 == 0:
        print(1)
    else:
        print(0)

a = int(input())
solution(a)


## no_2884
# 알람 시계

hour, minute = map(int, input().split())

total = hour*60 + minute

result = total - 45

new_hour = result // 60
new_minute = result % 60

if new_hour < 0:
    new_hour = 23

print(new_hour, new_minute, end=" ")


## no_9498
# 시험 성적

def solution(n):
    if 100 >= n >= 90:
        print("A")
    elif n >= 80:
        print("B")
    elif n >= 70:
        print("C")
    elif n >= 60:
        print("D")
    else:
        print("F")

a = int(input())
solution(a)


