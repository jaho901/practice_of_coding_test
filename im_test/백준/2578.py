import sys
sys.stdin = open('2578.txt')

data = [list(map(int, input().split())) for _ in range(5)]

arr = []
for _ in range(5):
    a = list(map(int, input().split()))
    arr += a
# 최종 결과값 저장
result = 0
# 행 저장
result1 = [0]*5
# 열 저장
result2 = [0]*5
# 정대각선 저장
result3 = [0]
# 역대각선 저장
result4 = [0]

for k in range(len(arr)):
    a = True
    for i in range(len(data)):
        for j in range(len(data[0])):
            # 사회자가 부른 수가 빙고에 있으면
            if data[i][j] == arr[k]:
                # 해당 열과 행에 1씩 추가
                result1[i] += 1
                result2[j] += 1
                # 정대각선이면
                if i == j:
                    result3[0] += 1
                # 역대각선이면
                if i == 5-j-1:
                    result4[0] += 1
                # 하나의 값을 찾으면 그 뒤로 반복문을 돌릴 필요가 없으니 아래와 같이 지정
                a = False
                break
        if not a:
            break
    # 사회자가 부른 수마다 계속 비교해준다.
    # 예를 들어 result1에서 하나의 값이 5가 됬다면 그 행은 빙고라는 뜻이다!
    # 그렇게 5라는 값이 3개 이상이 되면 멈춘다!!
    if result1.count(5) + result2.count(5) + result3.count(5) + result4.count(5) >= 3:
        result = k
        break
print(result+1)
