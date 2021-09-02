# 숫자 카드 게임
# N x M 행렬에서 각행에서의 최솟값들을 구한 다음 그 중에서의 최댓값 반환

n, m = map(int, input().split())

result = 0

# 한줄씩 입력받기
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)


