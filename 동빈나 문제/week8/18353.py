
N = int(input())
data = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(len(data) - max(dp))
