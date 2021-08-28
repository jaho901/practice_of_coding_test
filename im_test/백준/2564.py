import sys
sys.stdin = open('2564.txt')

w, h = map(int, input().split())
N = int(input())
result = 0
data = []
# 상점의 위치
for _ in range(N):
    data.append(list(map(int, input().split())))
# 현재 내 위치
now = list(map(int, input().split()))

# 현재 내 위치와 상점의 위치를 비교하면서 식을 작성해보자!!!
for i in data:
    # 현재 내 위치가 북쪽인 경우
    if now[0] == 1:
        # 상점의 위치가 북쪽인 경우
        if i[0] == 1:
            result += abs(now[1] - i[1])
        # 상점의 위치가 남쪽인 경우
        elif i[0] == 2:
            a = now[1] + h + i[1]
            b = (w - now[1]) + h + (w - i[1])
            result += min(a, b)
        # 상점의 위치가 서쪽인 경우
        elif i[0] == 3:
            result += now[1] + i[1]
        # 상점의 위치가 동쪽인 경우
        else:
            result += (w - now[1]) + i[1]

    # 현재 내 위치가 남쪽인 경우 (안에 조건문은 위와 동일함)
    elif now[0] == 2:
        if i[0] == 2:
            result += abs(now[1] - i[1])
        elif i[0] == 1:
            a = now[1] + h + i[1]
            b = (w - now[1]) + h + (w - i[1])
            result += min(a, b)
        elif i[0] == 3:
            result += now[1] + (h - i[1])
        else:
            result += (w - now[1]) + (h - i[1])

    # 현재 내 위치가 서쪽인 경우
    elif now[0] == 3:
        if i[0] == 3:
            result += abs(now[1] - i[1])
        elif i[0] == 4:
            a = now[1] + w + i[1]
            b = (h - now[1]) + w + (h - i[1])
            result += min(a, b)
        elif i[0] == 1:
            result += now[1] + i[1]
        else:
            result += (h - now[1]) + i[1]

    # 현재 내 위치가 동쪽인 경우
    elif now[0] == 4:
        if i[0] == 4:
            result += abs(now[1] - i[1])
        elif i[0] == 3:
            a = now[1] + w + i[1]
            b = (h - now[1]) + w + (h - i[1])
            result += min(a, b)
        elif i[0] == 1:
            result += now[1] + (w - i[1])
        else:
            result += (h - now[1]) + (w - i[1])

print(result)