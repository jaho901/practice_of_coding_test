import sys
sys.stdin = open('1244.txt')

N = int(input())
data = list(map(int, input().split()))

s_N = int(input())
student = [list(map(int, input().split())) for _ in range(s_N)]
data.insert(0,0)

for i in student:
    n = i[1]    
    # 남자인 경우
    if i[0] == 1:
        k = n
        # 가장 마지막으로 이동할때까지
        while n < len(data):
            if data[n] == 1:
                data[n] = 0
            else:
                data[n] = 1
            # n의 배수만큼 계속 상승시키기
            n += k

    # 여자인 경우
    elif i[0] == 2:
        k = 0
        while True:
            # 범위내에 존재하면서 k라는 기점을 중심으로 좌우가 같은 경우
            if n-k > 0 and n+k < len(data) and data[n-k] == data[n+k]:
                if data[n-k] == 1:
                    data[n-k] = 0
                    data[n+k] = 0
                else:
                    data[n-k] = 1
                    data[n+k] = 1
            # 달라지게 되면 곧바로 종료시킨다.
            else:
                break
            # 1씩 키워주면서 좌우를 비교
            k += 1
data = data[1:]

# 20줄씩 출력
while True:
    if len(data) > 20:
        print(*data[0:20])
        del data[0:20]
    else:
        print(*data[0:])
        break












