# for i in range(N):
#   for j in range(i+1, N):
#       if i != j:
#           조합

def solution(num, ball):
    # 필수 변수 지정
    N, M = map(int, num.split())
    ball = list(map(int, ball.split()))
    result = 0

    for i in range(len(ball)):
        for j in range(i+1, len(ball)):
            if ball[i] != ball[j]:
                result += 1

    return result



a = input()
b = input()
print(solution(a, b))









