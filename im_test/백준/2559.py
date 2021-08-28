import sys
sys.stdin = open('2559.txt')

N, K = map(int, input().split())
data = list(map(int, input().split()))

# 계속해서 비교해주기 위해 지정
result = sum(data[0:K])
total = sum(data[0:K])

for i in range(1, N-K+1):
    # 가장 처음 존재하는 값을 빼주고 다음 1개의 값을 더해주면서
    # 총 K개의 값들을 계속해서 비교해준다.
    total -= data[i-1]
    total += data[i+K-1]
    # 그때마다 계속해서 result와 비교해주고
    # 만약에 result보다 더 큰값을 가지면 그 값을 result로 지정
    if result < total:
        result = total

print(result)

# 예를 들어서,
# 데이터 == 3 -2 -4 -9 0 3 7 13 8 -3
# i = 1인 경우
# [3, -2]
# i = 2인 경우
# 1. 3을 뺀다 => [-2]
# 2. 다음 값을 더해준다. => [-2, -4]
# 이런식으로 리스트 길이를 K로 유지해주면서 한칸씩 이동하고 계속해서 비교해준다.
