import sys
sys.stdin = open('2304.txt', encoding='UTF-8')

N = int(input())
result = 0
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
# 데이터를 순서대로 정렬시켰다.
data = sorted(data)
# 기둥들이 존재하는 위치를 idx로 저장
idx = [i[0] for i in data]
# 각 기둥들의 높이를 value에 저장
value = [i[1] for i in data]
n = 0
# 밑에서 value1의 값을 바꿔줘야하기 때문에 얕은 복사 실시!
value1 = value[:]
# 벽돌들 중에 가장 큰 위치를 넣고
# 그 위치 이후에 나오는 값들중에서의 최댓값을 넣고
# 이것들을 끝까지 한 리스트 max_1 생성
max_1 = []
for i in range(len(value1)):
    # 계속해서 max값을 초기화
    maximum = max(value1)
    # i가 커감에 따라 maximum이면 max_1에 추가하고 그 값을 0으로 만들어준다.
    # 0으로 만들어주면 ==> 그 maximum 이후에 있는 값들 중에서 또 최댓값을 찾아 반복
    if value1[i] == maximum:
        max_1.append(i)
        value1[i] = 0
    # 지나간 곳은 무조건 0으로 바꿈
    else:
        value1[i] = 0

# 가장 처음 기둥의 높이
height = value[0]
# 가장 높은 기둥의 높이
maximum = max(value)
# 가장 높은 기둥의 위치
max_idx = value.index(maximum)
k = 0

# 마지막 기둥까지 실시
while k < N:
    # 가장 높은 기둥전까지
    if k < max_idx:
        # 다음 기둥의 높이가 현재 기둥보다 크면
        if height < value[k + 1]:
            # 가로 길이 n 추가해주고
            n += idx[k + 1] - idx[k]
            # 가로 * 세로 값을 result에 추가
            result += n * height
            # 현재 기둥 높이를 최신화시켜준다.
            height = value[k + 1]
            # 가로 또한 0으로 초기화
            n = 0
        # 다음 기둥의 높이가 작거나 같은 경우
        else:
            # 계속해서 가로길이 n에 추가해준다.
            n += idx[k + 1] - idx[k]
        # 어떤 경우든 k에 1씩 추가!
        k += 1

    # 가장 높은 기둥에 도착한 경우
    elif k == max_idx:
        # 그 기둥의 높이만을 result에 저장 (문제에서 그림1 보면서 이해하기!!)
        result += value[max_idx]
        n = 0
        # 해당하는 max값을 max_1 리스트에서 제거해주기!
        max_1.pop(0)
        k += 1

    # 가장 높은 기둥 이후의 상황!!
    else:
        # 다음으로 최댓값에 도착한다면
        if k == max_1[0]:
            # 다시 가로지정해서 넓이 result에 더해준다.
            n += idx[k] - idx[k-1]
            result += n * value[k]
            max_1.pop(0)
            n = 0
        else:
            n += idx[k] - idx[k-1]
        k += 1

print(result)

